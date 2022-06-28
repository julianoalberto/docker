FROM alpine:latest

ENTRYPOINT echo "[$(date)] $(hostname)" | tee -a /var/log/ctw.log
