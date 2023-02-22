echo "Here is some code."
echo "We wrote it in Bash."
echo "Bash is just a programming language, really."
# This is a comment.
# Let's read a file.
cat requirements.txt
# Do something extremely useful for continous deployment
git pull
# Hmmm, we should probably restart the application after we've pulled in
# new code, otherwise we can be looking for what went wrong for quite a
# while..
systemctl restart my-project