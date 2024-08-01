# CloudVisionTutorial
Google Cloud Vision API Setup Guide
This guide will walk you through the process of setting up a Google Service Account and configuring the Google Cloud Vision API. Follow the steps below to get started.

# Prerequisites
- A Google Cloud Platform (GCP) account.
- Basic knowledge of using the command line.
Steps
# 1. Create a Google Cloud Project
- Go to the Google Cloud Console.
- Click on the project drop-down and select "New Project".
- Enter a project name and select a billing account.
- Click "Create".
# 2. Enable the Google Cloud Vision API
- In the Google Cloud Console, select your project.
- Navigate to the "API & Services" > "Library".
- Search for "Cloud Vision API".
- Click on "Cloud Vision API" and then click "Enable".
# 3. Create a Service Account
- In the Google Cloud Console, navigate to "IAM & Admin" > "Service Accounts".
- Click on "Create Service Account".
- Enter a name and description for the service account.
- Click "Create".
- In the "Service account permissions" step, select the "Project" > "Editor" role (or any role that suits your needs).
- Click "Continue".
- Click "Done".
# 4. Create and Download a Service Account Key
- In the Google Cloud Console, navigate to "IAM & Admin" > "Service Accounts".
- Find your service account and click on the three dots under "Actions".
- Select "Manage keys".
- Click on "Add Key" > "Create new key".
- Select "JSON" as the key type.
- Click "Create". A JSON file will be downloaded to your computer. Keep this file secure, as it contains your service account credentials.