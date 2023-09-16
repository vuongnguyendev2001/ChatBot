from rasa.callbacks import Callback
import os


class MyCallback(Callback):
    def on_epoch_end(self, epoch, logs=None):
        if logs is not None:
            loss = logs.get("loss")
            accuracy = logs.get("accuracy")

            # Lưu lại loss và accuracy vào tập tin
            with open("train_metrics.txt", "a") as file:
                file.write(f"Epoch {epoch + 1}: Loss={loss}, Accuracy={accuracy}\n")


# Sử dụng callback trong quá trình train
callback = MyCallback()
