import requests

# Define your Jenkins URL and credentials
jenkins_url = 'http://your-jenkins-url/'
username = 'your-username'
password = 'your-password'

# Create a session with Jenkins to handle authentication
session = requests.Session()
session.auth = (username, password)

# Function to list all pipelines/jobs
def list_pipelines():
    job_url = jenkins_url + 'api/json?tree=jobs[name]'
    response = session.get(job_url)
    jobs = response.json()['jobs']
    pipeline_names = [job['name'] for job in jobs]
    return pipeline_names

# Function to list all credentials (requires Jenkins Credentials Plugin)
def list_credentials():
    credentials_url = jenkins_url + 'credentials/store/system/domain/_/api/json?tree=credentials[id]'
    response = session.get(credentials_url)
    credentials = response.json()['credentials']
    credential_ids = [cred['id'] for cred in credentials]
    return credential_ids

# Function to list all nodes (agents)
def list_nodes():
    nodes_url = jenkins_url + 'computer/api/json?tree=computer[displayName]'
    response = session.get(nodes_url)
    nodes = response.json()['computer']
    node_names = [node['displayName'] for node in nodes]
    return node_names

# Function to list all installed plugins
def list_plugins():
    plugins_url = jenkins_url + 'pluginManager/api/json?tree=plugins[shortName,version]'
    response = session.get(plugins_url)
    plugins = response.json()['plugins']
    plugin_list = [(plugin['shortName'], plugin['version']) for plugin in plugins]
    return plugin_list

# Main function to gather and display information
def main():
    print("Pipeline Names:")
    for pipeline in list_pipelines():
        print(pipeline)

    print("\nCredentials IDs:")
    for credential_id in list_credentials():
        print(credential_id)

    print("\nNodes (Agents):")
    for node_name in list_nodes():
        print(node_name)

    print("\nInstalled Plugins:")
    for plugin, version in list_plugins():
        print(f"{plugin} - {version}")

if __name__ == "__main__":
    main()


########################################################################

# Categorize 

########################################################################

import requests

# Define your Jenkins URL and credentials
jenkins_url = 'http://your-jenkins-url/'
username = 'your-username'
password = 'your-password'

# Create a session with Jenkins to handle authentication
session = requests.Session()
session.auth = (username, password)

# Function to list all jobs
def list_jobs():
    job_url = jenkins_url + 'api/json?tree=jobs[name,displayName,_class]'
    response = session.get(job_url)
    jobs = response.json()['jobs']
    return jobs

# Categorize jobs into multiline pipelines, folders, and standalone jobs
def categorize_jobs(jobs):
    multiline_pipelines = []
    folders = []
    standalone_jobs = []

    for job in jobs:
        job_name = job['name']
        job_display_name = job['displayName']
        job_class = job['_class']

        if job_class == 'com.cloudbees.hudson.plugins.folder.Folder':
            folders.append(job_display_name)
        elif job_class == 'org.jenkinsci.plugins.workflow.multibranch.WorkflowMultiBranchProject':
            multiline_pipelines.append(job_display_name)
        else:
            standalone_jobs.append(job_display_name)

    return multiline_pipelines, folders, standalone_jobs

# Main function to gather and display categorized information
def main():
    jobs = list_jobs()
    multiline_pipelines, folders, standalone_jobs = categorize_jobs(jobs)

    print("Multiline Pipelines:")
    for pipeline in multiline_pipelines:
        print(pipeline)

    print("\nFolders:")
    for folder in folders:
        print(folder)

    print("\nStandalone Jobs:")
    for job in standalone_jobs:
        print(job)

if __name__ == "__main__":
    main()

