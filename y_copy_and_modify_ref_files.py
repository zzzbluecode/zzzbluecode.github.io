import os

# Change the current working directory to the directory of the script
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Define the source and destination directories
ref_dir = './ref'
dest_dir = './'

import re

def replace_last_div_outside_script(text, new_word):
    # Regex to match <script> blocks
    script_pattern = re.compile(r'<script.*?>.*?</script>', re.DOTALL)
    
    # Find all <script> blocks and their positions
    script_blocks = list(script_pattern.finditer(text))
    
    # Find all occurrences of </div>
    div_matches = list(re.finditer(r'</div>', text))
    
    # Iterate through </div> matches in reverse order
    for match in reversed(div_matches):
        # Check if the match is inside any <script> block
        inside_script = False
        for script_block in script_blocks:
            if script_block.start() <= match.start() <= script_block.end():
                inside_script = True
                break
        
        # If not inside a <script> block, replace it
        if not inside_script:
            start, end = match.span()
            return text[:start] + new_word + text[end:]
    
    # If no valid </div> found, return the original text
    return text

def add_page_to_left_panel(page_name):
    page_to_add = f'<li><a href="{page_name}">{page_name.replace("page_", "", 1).replace(".html", "")}</a></li>'
    
    # Read the content of left-panel.html
    with open('left-panel.html', 'r') as left_panel_file:
        left_panel_content = left_panel_file.read()
    
    # Check if the page is already present
    if page_to_add not in left_panel_content:
        # Insert the new page below the comment
        left_panel_content = left_panel_content.replace('<!-- add page end -->', f'{page_to_add}\n            <!-- add page end -->')
        
        # Write the modified content back to left-panel.html
        with open('left-panel.html', 'w') as left_panel_file:
            left_panel_file.write(left_panel_content)

# Iterate over all files in the ref directory
for filename in os.listdir(ref_dir):
    if filename.endswith('.html') and "copy" not in filename:
        source_file_path = os.path.join(ref_dir, filename)
        dest_file_path = os.path.join(dest_dir, f"page_{filename}")
        
        # Read the content of the source file
        with open(source_file_path, 'r') as source_file:
            content = source_file.read()
            
        # Modify the content as needed
        content = content.replace('<style>', '<link rel="stylesheet" href="styles.css?1737904956">\n    <style>')
        content = content.replace('body {', '/* body {')
        content = content.replace('}', '} */', 1)
        content = content.replace('<body>', '<body>\n<div id="left-panel-placeholder"></div>\n<div class="main-content">')
        content = content.replace('</body>', '<script src="script.js"></script>\n</body>')
        content = replace_last_div_outside_script(content, "</div>\n</div>")

        # Write the modified content to the destination file
        with open(dest_file_path, 'w') as dest_file:
            dest_file.write(content)

        print(f"File '{filename}' copied to '{dest_file_path}'")
        add_page_to_left_panel(f"page_{filename}")
        print(f"Page '{filename}' added to the left panel")
