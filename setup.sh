mkdir -p ~/.streamlit/

echo "
[general]
email = \"<myemail@domain>\"
" > ~/.streamlit/credentials.toml

echo "[server]
headless = true
port = $PORT
enableCORS = false
" > ~/.streamlit/config.toml