ZIP=python.zip
FUNCTION_NAME=bolt-smart-home

rm $ZIP
cd python
zip ../$ZIP *
cd .. 
aws lambda update-function-code --function-name $FUNCTION_NAME --zip-file fileb://$ZIP
