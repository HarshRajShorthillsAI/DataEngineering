#!/bin/sh
echo "Writing multiple lines to a document using heredoc"

var=$(cat <<EOF
Hello, How are you?
Nice Thank you.
Talk to you later.
Bye
EOF
)

echo "$var"

var=$(cat <<EOF > mytext.txt
Hello, How are you?
Nice Thank you.
Talk to you later.
Bye
This text is saved to file using heredoc
EOF
)

echo "$var"