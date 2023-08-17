#!/bin/bash
echo "[task.sh] [1/3] Starting Execution."

# Download json containing file paths of uploaded files
# If no url is specified use default.json 
echo "[task.sh] [2/3] Downloading upload.json"
# Check if the environmental variable JSON_URL is set
if [ -z "$JSON_URL" ]; then
    echo "Environmental variable JSON_URL is not set. Using default."
else
	# Use wget to download the JSON file
	output_file="data/upload.json"
	wget -O "$output_file" "$JSON_URL"

	# Check if the download was successful
	if [ $? -eq 0 ]; then
		echo "JSON file downloaded successfully."
	else
		echo "Failed to download JSON file. Using default."
	fi
fi

echo "[task.sh] [3/3] Checking Files"
python3 scripts/tapis_file_lister.py

echo "[task.sh] All done!"