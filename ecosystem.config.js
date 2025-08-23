module.exports = {
  apps: [
    {
      name: "tgbot-example",
      script: "poetry",
      args: "run python3 main.py",
      interpreter: "none", // because poetry start by itself
      watch: false,
      autorestart: true,
      max_restarts: 5,
      log_date_format: "YYYY-MM-DD HH:mm:ss",
      error_file: "./logs/err.log",
      out_file: "./logs/out.log",
      merge_logs: true,
      env: {
        ENV: "production"
      }
    }
  ]
};
