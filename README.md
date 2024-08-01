# Google Cloud Vision API Setup Guide

This guide will walk you through the process of setting up a Google Service Account and configuring the Google Cloud Vision API. Follow the steps below to get started.

## Prerequisites

- A Google Cloud Platform (GCP) account.
- Basic knowledge of using the command line.

## Steps

### 1. Create a Google Cloud Project

1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
2. Click on the project drop-down and select "New Project".
3. Enter a project name and select a billing account.
4. Click "Create".

### 2. Enable the Google Cloud Vision API

1. In the [Google Cloud Console](https://console.cloud.google.com/), select your project.
2. Navigate to the "API & Services" > "Library".
3. Search for "Cloud Vision API".
4. Click on "Cloud Vision API" and then click "Enable".

### 3. Create a Service Account

1. In the [Google Cloud Console](https://console.cloud.google.com/), navigate to "IAM & Admin" > "Service Accounts".
2. Click on "Create Service Account".
3. Enter a name and description for the service account.
4. Click "Create".
5. In the "Service account permissions" step, select the "Project" > "Editor" role (or any role that suits your needs).
6. Click "Continue".
7. Click "Done".

### 4. Create and Download a Service Account Key

1. In the [Google Cloud Console](https://console.cloud.google.com/), navigate to "IAM & Admin" > "Service Accounts".
2. Find your service account and click on the three dots under "Actions".
3. Select "Manage keys".
4. Click on "Add Key" > "Create new key".
5. Select "JSON" as the key type.
6. Click "Create". A JSON file will be downloaded to your computer. Keep this file secure, as it contains your service account credentials.

### 5. Set Up Authentication

1. Set the `GOOGLE_APPLICATION_CREDENTIALS` environment variable to the file path of the JSON file you downloaded.
   - On Windows:
     ```sh
     set GOOGLE_APPLICATION_CREDENTIALS="[PATH_TO_JSON_FILE]"
     ```
   - On macOS/Linux:
     ```sh
     export GOOGLE_APPLICATION_CREDENTIALS="[PATH_TO_JSON_FILE]"
     ```

### 6. Install Google Cloud Vision Client Library

1. Install the Google Cloud Vision client library using pip:
   ```sh
   pip install google-cloud-vision
