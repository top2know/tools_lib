import yolov5

model = yolov5.load('yolov5m.pt')


def detect_objects(url, output_folder='output', to_print=False):
    results = model(url)
    if to_print:
        results.show()
    else:
        results.save(save_dir=output_folder)