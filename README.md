## Tapis File Tester

## How to Run

In order to run the container, an env file must be passed to the container.
Example:
```sh
# Tapis authentication parameters. All are mandatory.
TAPIS_BASE_URL=url
TAPIS_USERNAME=user
TAPIS_PASSWORD=password
TAPIS_TENANT_ID=user_id

# The container will send an email using SMTP with these parameters. Both are mandatory.
RECEIVER_EMAIL=user@hawaii.edu
EMAIL_SUBJECT=Tapis File Upload Errors

# The container will download a json from the specified url. This parameter is OPTIONAL.
# If no url is specified it will use a default json included in the container
JSON_URL=https://raw.githubusercontent.com/ikewai/rainfall/main/upload_configs/monthly/final_products.json
```

**Typical production run**

This executes the container with a specified environment file (see above)
```sh
docker run --env-file=.env file-tester     
```