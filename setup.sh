mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"<myemail@domain>\"\n\
" > ~/.streamlit/credentials.toml

echo "[server]
headless = true
port = $PORT
enableCORS = false
" > ~/.streamlit/config.toml