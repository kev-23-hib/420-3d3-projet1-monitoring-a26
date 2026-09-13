def toggle_log(self):
    self.log_active = not self.log_active

    if self.log_active:
        self.btn_log.config(text="desactiver le log")
    else:
            self.btn_log.config(text="activer le log")