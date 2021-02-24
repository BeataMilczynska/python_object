from lxml import etree


def check_bbox_fits_in(
    xmin: int,
    xmax: int,
    ymin: int,
    ymax: int,
    height_max: int,
    weidth_max: int,
    height_min: int = 0,
    weidth_min: int = 0,
):
    # Conditions below are buggy - but I have to leave something for you ;)
    if (xmin <= height_min and xmax <= height_max):
        print("OK")
    else:
        print("Objekt wykracza poza wysokość")

    if (ymin <= weidth_min and ymax <= weidth_max):
        print("OK")
    else:
        print("Objekt wykracza poza szerokość")


def get_bbox_points(bbox):
    # Possible improvement: you could create `BBox` class that would be returned here
    return [int(bbox.find(x).text) for x in ['xmin', 'xmax', 'ymin', 'ymax']]


def validate(file_path: str):
    tree = etree.parse(file_path)
    root = tree.getroot()
    size = root.find("size")
    # Get image width and height
    width = size.find("width").text
    height = size.find("height").text
    # Traverse through whole document and finds all elements with `bndbox` tag
    all_bboxes = root.findall(".//bndbox")

    for bbox in all_bboxes:
        xmin, xmax, ymin, ymax = get_bbox_points(bbox)
        check_bbox_fits_in(
            xmin=xmin,
            xmax=xmax,
            ymin=ymin,
            ymax=ymax,
            height_max=height,
            weidth_max=width,
        )


if __name__ == "__main__":
    """
    How to run:
        
        pip install lxml
        python3 validator.py
    
    Docs for lxml: https://lxml.de/
    
    """
    # Possible improvement: make fully fledged CLI tool using Typer https://github.com/tiangolo/typer
    validate("paslac_voc.xlm")  # For now let's have this path hardcoded
