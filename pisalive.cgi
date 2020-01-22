#!/bin/bash

echo -e "Content-type: text/html\n\n"

echo "<h1>Raspberry Pi Status: $(sp1b)</h1>"

echo "<h2>Who is logged in</h2>"
echo "<pre>$(./rpistatus)</pre>"



