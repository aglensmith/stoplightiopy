import stoplight
import zipfile


# HELPERS #####################################################################
def unzip_file(path_to_zip_file, directory_to_extract_to):
    with zipfile.ZipFile(path_to_zip_file, 'r') as zip_ref:
        zip_ref.extractall(directory_to_extract_to)

def handle_input():
    return

# either:
def download_stoplight_build(build_id):
    return

def extract_stoplight_build_zip(file_path):
    return

# or:
def http_get_static_data_from_live_site(domain_address):
    return

def combine_tree_data_json():
    """combines tree data objects from multiple json files into a single object"""
    return

def build_redirect_list(old_tree_data, new_tree_data):
    return

def backup_current_config(domain_id_or_address):
    return

def write_all_paths_to_txt(tree_data):
    """writes all paths in tree_data json to a txt file"""

def clean_existing_redirects(existing_redirects, new_redirects):
    return




