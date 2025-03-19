WIDTH = 16
HEIGHT = 32
FIRST = 0x20
LAST = 0x7f
_FONT = \
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x03\xc0\x03\xc0\x07\xe0\x07\xe0\x0f\xf0\x0f\xf0\x0f\xf0\x0f\xf0\x0f\xf0\x0f\xf0\x07\xe0\x07\xe0\x03\xc0\x03\xc0\x03\xc0\x03\xc0\x00\x00\x00\x00\x03\xc0\x03\xc0\x03\xc0\x03\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x3c\x3c\x3c\x3c\x3c\x3c\x3c\x3c\x1c\x38\x1c\x38\x0c\x30\x0c\x30\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1c\x38\x1c\x38\x1c\x38\x1c\x38\x7f\xfe\x7f\xfe\x1c\x38\x1c\x38\x1c\x38\x1c\x38\x1c\x38\x1c\x38\x1c\x38\x1c\x38\x7f\xfe\x7f\xfe\x1c\x38\x1c\x38\x1c\x38\x1c\x38\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x03\xc0\x03\xc0\x03\xc0\x03\xc0\x07\xe0\x07\xe0\x1e\x78\x1e\x78\x3c\x3c\x3c\x3c\x3c\x00\x3c\x00\x1e\x00\x1e\x00\x07\xe0\x07\xe0\x00\x78\x00\x78\x00\x3c\x00\x3c\x3c\x3c\x3c\x3c\x1e\x78\x1e\x78\x07\xe0\x07\xe0\x03\xc0\x03\xc0\x03\xc0\x03\xc0\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x3c\x3c\x3c\x3c\x3c\x78\x3c\x78\x00\xf0\x00\xf0\x01\xe0\x01\xe0\x03\xc0\x03\xc0\x07\x80\x07\x80\x0f\x00\x0f\x00\x1e\x3c\x1e\x3c\x3c\x3c\x3c\x3c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x07\xc0\x07\xc0\x1e\xf0\x1e\xf0\x3c\x78\x3c\x78\x1e\xf0\x1e\xf0\x07\xc0\x07\xc0\x0f\x9e\x0f\x9e\x3f\xfc\x3f\xfc\x78\xf8\x78\xf8\x78\x78\x78\x78\x3c\xfc\x3c\xfc\x0f\x9e\x0f\x9e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x0f\x00\x0f\x00\x0f\x00\x0f\x00\x0f\x00\x0f\x00\x1e\x00\x1e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x01\xe0\x01\xe0\x03\xc0\x03\xc0\x07\x80\x07\x80\x0f\x00\x0f\x00\x0f\x00\x0f\x00\x0f\x00\x0f\x00\x0f\x00\x0f\x00\x0f\x00\x0f\x00\x07\x80\x07\x80\x03\xc0\x03\xc0\x01\xe0\x01\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x01\xe0\x01\xe0\x00\xf0\x00\xf0\x00\x78\x00\x78\x00\x3c\x00\x3c\x00\x3c\x00\x3c\x00\x3c\x00\x3c\x00\x3c\x00\x3c\x00\x3c\x00\x3c\x00\x78\x00\x78\x00\xf0\x00\xf0\x01\xe0\x01\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x3c\x3c\x3c\x3c\x0f\xf0\x0f\xf0\x7f\xfe\x7f\xfe\x0f\xf0\x0f\xf0\x3c\x3c\x3c\x3c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\xc0\x03\xc0\x03\xc0\x03\xc0\x03\xc0\x03\xc0\x7f\xfe\x7f\xfe\x03\xc0\x03\xc0\x03\xc0\x03\xc0\x03\xc0\x03\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\xc0\x03\xc0\x03\xc0\x03\xc0\x03\x80\x03\x80\x07\x00\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x7f\xfe\x7f\xfe\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\xc0\x03\xc0\x03\xc0\x03\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x3c\x00\x3c\x00\x78\x00\x78\x00\xf0\x00\xf0\x01\xe0\x01\xe0\x03\xc0\x03\xc0\x07\x80\x07\x80\x0f\x00\x0f\x00\x1e\x00\x1e\x00\x3c\x00\x3c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x07\xe0\x07\xe0\x1e\x78\x1e\x78\x3c\x3c\x3c\x3c\x3c\x7c\x3c\x7c\x3c\xfc\x3c\xfc\x3d\xbc\x3d\xbc\x3f\x3c\x3f\x3c\x3e\x3c\x3e\x3c\x3c\x3c\x3c\x3c\x1e\x78\x1e\x78\x07\xe0\x07\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x03\xc0\x03\xc0\x0f\xc0\x0f\xc0\x3f\xc0\x3f\xc0\x03\xc0\x03\xc0\x03\xc0\x03\xc0\x03\xc0\x03\xc0\x03\xc0\x03\xc0\x03\xc0\x03\xc0\x03\xc0\x03\xc0\x03\xc0\x03\xc0\x3f\xfc\x3f\xfc\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0f\xe0\x0f\xe0\x3c\x78\x3c\x78\x00\x3c\x00\x3c\x00\x3c\x00\x3c\x00\x78\x00\x78\x00\xf0\x00\xf0\x03\xc0\x03\xc0\x0f\x00\x0f\x00\x1e\x00\x1e\x00\x3c\x3c\x3c\x3c\x3f\xfc\x3f\xfc\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0f\xf0\x0f\xf0\x3c\x3c\x3c\x3c\x00\x1e\x00\x1e\x00\x1e\x00\x1e\x00\x3c\x00\x3c\x03\xf0\x03\xf0\x00\x3c\x00\x3c\x00\x1e\x00\x1e\x00\x1e\x00\x1e\x3c\x3c\x3c\x3c\x0f\xf0\x0f\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x01\xf0\x01\xf0\x03\xf0\x03\xf0\x07\xf0\x07\xf0\x0f\xf0\x0f\xf0\x1e\xf0\x1e\xf0\x3c\xf0\x3c\xf0\x3f\xfc\x3f\xfc\x00\xf0\x00\xf0\x00\xf0\x00\xf0\x00\xf0\x00\xf0\x03\xfc\x03\xfc\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x3f\xfe\x3f\xfe\x3c\x00\x3c\x00\x3c\x00\x3c\x00\x3c\x00\x3c\x00\x3f\xf0\x3f\xf0\x00\x3c\x00\x3c\x00\x1e\x00\x1e\x00\x1e\x00\x1e\x00\x1e\x00\x1e\x3c\x3c\x3c\x3c\x0f\xf0\x0f\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x07\xf0\x07\xf0\x1e\x00\x1e\x00\x3c\x00\x3c\x00\x3c\x00\x3c\x00\x3c\x00\x3c\x00\x3f\xf0\x3f\xf0\x3c\x3c\x3c\x3c\x3c\x1e\x3c\x1e\x3c\x1e\x3c\x1e\x1e\x3c\x1e\x3c\x07\xf0\x07\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x3f\xfc\x3f\xfc\x3c\x3c\x3c\x3c\x00\x3c\x00\x3c\x00\x78\x00\x78\x00\xf0\x00\xf0\x01\xe0\x01\xe0\x03\xc0\x03\xc0\x03\xc0\x03\xc0\x03\xc0\x03\xc0\x03\xc0\x03\xc0\x03\xc0\x03\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x07\xf0\x07\xf0\x1e\x3c\x1e\x3c\x3c\x1e\x3c\x1e\x3c\x1e\x3c\x1e\x1e\x3c\x1e\x3c\x07\xf0\x07\xf0\x1e\x3c\x1e\x3c\x3c\x1e\x3c\x1e\x3c\x1e\x3c\x1e\x1e\x3c\x1e\x3c\x07\xf0\x07\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x07\xf0\x07\xf0\x1e\x3c\x1e\x3c\x3c\x1e\x3c\x1e\x3c\x1e\x3c\x1e\x1e\x1e\x1e\x1e\x07\xfe\x07\xfe\x00\x1e\x00\x1e\x00\x1e\x00\x1e\x00\x1e\x00\x1e\x00\x3c\x00\x3c\x0f\xf0\x0f\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\xc0\x03\xc0\x03\xc0\x03\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\xc0\x03\xc0\x03\xc0\x03\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\xc0\x03\xc0\x03\xc0\x03\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\xc0\x03\xc0\x03\xc0\x03\xc0\x07\x80\x07\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x01\xe0\x01\xe0\x03\xc0\x03\xc0\x07\x80\x07\x80\x0f\x00\x0f\x00\x1e\x00\x1e\x00\x3c\x00\x3c\x00\x1e\x00\x1e\x00\x0f\x00\x0f\x00\x07\x80\x07\x80\x03\xc0\x03\xc0\x01\xe0\x01\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x3f\xfc\x3f\xfc\x00\x00\x00\x00\x00\x00\x00\x00\x3f\xfc\x3f\xfc\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x07\x80\x07\x80\x03\xc0\x03\xc0\x01\xe0\x01\xe0\x00\xf0\x00\xf0\x00\x78\x00\x78\x00\x3c\x00\x3c\x00\x78\x00\x78\x00\xf0\x00\xf0\x01\xe0\x01\xe0\x03\xc0\x03\xc0\x07\x80\x07\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x07\xe0\x07\xe0\x1e\x78\x1e\x78\x3c\x3c\x3c\x3c\x00\x78\x00\x78\x00\xf0\x00\xf0\x01\xe0\x01\xe0\x03\xc0\x03\xc0\x03\xc0\x03\xc0\x00\x00\x00\x00\x03\xc0\x03\xc0\x03\xc0\x03\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0f\xfc\x0f\xfc\x3c\x1e\x3c\x1e\x78\x1e\x78\x1e\x79\xfe\x79\xfe\x7b\x8e\x7b\x8e\x7b\x8e\x7b\x8e\x7b\x8e\x7b\x8e\x79\xfc\x79\xfc\x78\x00\x78\x00\x3c\x00\x3c\x00\x0f\xfc\x0f\xfc\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x03\xc0\x03\xc0\x07\xe0\x07\xe0\x0f\xf0\x0f\xf0\x1e\x78\x1e\x78\x3c\x3c\x3c\x3c\x3c\x3c\x3c\x3c\x3f\xfc\x3f\xfc\x3c\x3c\x3c\x3c\x3c\x3c\x3c\x3c\x3c\x3c\x3c\x3c\x3c\x3c\x3c\x3c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x7f\xf0\x7f\xf0\x1e\x3c\x1e\x3c\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x3c\x1e\x3c\x1f\xf0\x1f\xf0\x1e\x3c\x1e\x3c\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x3c\x1e\x3c\x7f\xf0\x7f\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x07\xf0\x07\xf0\x1e\x3c\x1e\x3c\x3c\x1e\x3c\x1e\x3c\x00\x3c\x00\x3c\x00\x3c\x00\x3c\x00\x3c\x00\x3c\x00\x3c\x00\x3c\x00\x3c\x00\x3c\x1e\x3c\x1e\x1e\x3c\x1e\x3c\x07\xf0\x07\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x7f\xf0\x7f\xf0\x1e\x3c\x1e\x3c\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x3c\x1e\x3c\x7f\xf0\x7f\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x7f\xfe\x7f\xfe\x1e\x0e\x1e\x0e\x1e\x06\x1e\x06\x1e\x00\x1e\x00\x1e\x60\x1e\x60\x1f\xe0\x1f\xe0\x1e\x60\x1e\x60\x1e\x00\x1e\x00\x1e\x06\x1e\x06\x1e\x0e\x1e\x0e\x7f\xfe\x7f\xfe\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x7f\xfe\x7f\xfe\x1e\x0e\x1e\x0e\x1e\x06\x1e\x06\x1e\x00\x1e\x00\x1e\x60\x1e\x60\x1f\xe0\x1f\xe0\x1e\x60\x1e\x60\x1e\x00\x1e\x00\x1e\x00\x1e\x00\x1e\x00\x1e\x00\x7f\x80\x7f\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x07\xf0\x07\xf0\x1e\x3c\x1e\x3c\x3c\x1e\x3c\x1e\x3c\x00\x3c\x00\x3c\x00\x3c\x00\x3c\x00\x3c\x00\x3c\x7e\x3c\x7e\x3c\x1e\x3c\x1e\x3c\x1e\x3c\x1e\x1e\x3e\x1e\x3e\x07\xf6\x07\xf6\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x3c\x1e\x3c\x1e\x3c\x1e\x3c\x1e\x3c\x1e\x3c\x1e\x3c\x1e\x3c\x1e\x3c\x1e\x3c\x1e\x3f\xfe\x3f\xfe\x3c\x1e\x3c\x1e\x3c\x1e\x3c\x1e\x3c\x1e\x3c\x1e\x3c\x1e\x3c\x1e\x3c\x1e\x3c\x1e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0f\xf0\x0f\xf0\x03\xc0\x03\xc0\x03\xc0\x03\xc0\x03\xc0\x03\xc0\x03\xc0\x03\xc0\x03\xc0\x03\xc0\x03\xc0\x03\xc0\x03\xc0\x03\xc0\x03\xc0\x03\xc0\x03\xc0\x03\xc0\x0f\xf0\x0f\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x03\xfe\x03\xfe\x00\x78\x00\x78\x00\x78\x00\x78\x00\x78\x00\x78\x00\x78\x00\x78\x00\x78\x00\x78\x00\x78\x00\x78\x00\x78\x00\x78\x3c\x78\x3c\x78\x1f\xf0\x1f\xf0\x07\xc0\x07\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x7e\x3c\x7e\x3c\x1e\x78\x1e\x78\x1e\xf0\x1e\xf0\x1f\xe0\x1f\xe0\x1f\xc0\x1f\xc0\x1f\xc0\x1f\xc0\x1f\xe0\x1f\xe0\x1e\xf0\x1e\xf0\x1e\x78\x1e\x78\x1e\x3c\x1e\x3c\x7e\x1e\x7e\x1e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x7f\x80\x7f\x80\x1e\x00\x1e\x00\x1e\x00\x1e\x00\x1e\x00\x1e\x00\x1e\x00\x1e\x00\x1e\x00\x1e\x00\x1e\x00\x1e\x00\x1e\x00\x1e\x00\x1e\x06\x1e\x06\x1e\x0e\x1e\x0e\x7f\xfe\x7f\xfe\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x78\x1e\x78\x1e\x7c\x3e\x7c\x3e\x7e\x7e\x7e\x7e\x7f\xfe\x7f\xfe\x7b\xde\x7b\xde\x79\x9e\x79\x9e\x78\x1e\x78\x1e\x78\x1e\x78\x1e\x78\x1e\x78\x1e\x78\x1e\x78\x1e\x78\x1e\x78\x1e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x3c\x1e\x3c\x1e\x3c\x1e\x3c\x1e\x3e\x1e\x3e\x1e\x3f\x1e\x3f\x1e\x3f\x9e\x3f\x9e\x3d\xde\x3d\xde\x3c\xfe\x3c\xfe\x3c\x7e\x3c\x7e\x3c\x3e\x3c\x3e\x3c\x1e\x3c\x1e\x3c\x1e\x3c\x1e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x07\xf0\x07\xf0\x1e\x3c\x1e\x3c\x3c\x1e\x3c\x1e\x3c\x1e\x3c\x1e\x3c\x1e\x3c\x1e\x3c\x1e\x3c\x1e\x3c\x1e\x3c\x1e\x3c\x1e\x3c\x1e\x3c\x1e\x3c\x1e\x1e\x3c\x1e\x3c\x07\xf0\x07\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x7f\xf0\x7f\xf0\x1e\x3c\x1e\x3c\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x3c\x1e\x3c\x1f\xf0\x1f\xf0\x1e\x00\x1e\x00\x1e\x00\x1e\x00\x1e\x00\x1e\x00\x1e\x00\x1e\x00\x7f\x80\x7f\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x07\xf0\x07\xf0\x1e\x3c\x1e\x3c\x3c\x1e\x3c\x1e\x3c\x1e\x3c\x1e\x3c\x1e\x3c\x1e\x3c\x1e\x3c\x1e\x3c\x1e\x3c\x1e\x3d\xde\x3d\xde\x3c\xfe\x3c\xfe\x1e\x7c\x1e\x7c\x07\xf8\x07\xf8\x00\x1c\x00\x1c\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x7f\xf0\x7f\xf0\x1e\x3c\x1e\x3c\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x3c\x1e\x3c\x1f\xf0\x1f\xf0\x1f\xe0\x1f\xe0\x1e\xf0\x1e\xf0\x1e\x78\x1e\x78\x1e\x3c\x1e\x3c\x7e\x1e\x7e\x1e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0f\xf0\x0f\xf0\x3c\x3c\x3c\x3c\x78\x1e\x78\x1e\x3c\x00\x3c\x00\x0f\x00\x0f\x00\x03\xc0\x03\xc0\x00\xf0\x00\xf0\x00\x3c\x00\x3c\x78\x1e\x78\x1e\x3c\x3c\x3c\x3c\x0f\xf0\x0f\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x7f\xfe\x7f\xfe\x73\xce\x73\xce\x63\xc6\x63\xc6\x03\xc0\x03\xc0\x03\xc0\x03\xc0\x03\xc0\x03\xc0\x03\xc0\x03\xc0\x03\xc0\x03\xc0\x03\xc0\x03\xc0\x03\xc0\x03\xc0\x0f\xf0\x0f\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x3c\x1e\x3c\x1e\x3c\x1e\x3c\x1e\x3c\x1e\x3c\x1e\x3c\x1e\x3c\x1e\x3c\x1e\x3c\x1e\x3c\x1e\x3c\x1e\x3c\x1e\x3c\x1e\x3c\x1e\x3c\x1e\x3c\x1e\x3c\x1e\x1e\x3c\x1e\x3c\x07\xf0\x07\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x3c\x3c\x3c\x3c\x3c\x3c\x3c\x3c\x3c\x3c\x3c\x3c\x3c\x3c\x3c\x3c\x3c\x3c\x3c\x3c\x3c\x3c\x3c\x3c\x3c\x3c\x3c\x3c\x1e\x78\x1e\x78\x0f\xf0\x0f\xf0\x07\xe0\x07\xe0\x03\xc0\x03\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x78\x1e\x78\x1e\x78\x1e\x78\x1e\x78\x1e\x78\x1e\x78\x1e\x78\x1e\x78\x1e\x78\x1e\x78\x1e\x78\x1e\x79\x9e\x79\x9e\x7b\xde\x7b\xde\x7f\xfe\x7f\xfe\x3e\x7c\x3e\x7c\x1c\x38\x1c\x38\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x3c\x3c\x3c\x3c\x3c\x3c\x3c\x3c\x1e\x78\x1e\x78\x0f\xf0\x0f\xf0\x07\xe0\x07\xe0\x03\xc0\x03\xc0\x07\xe0\x07\xe0\x0f\xf0\x0f\xf0\x1e\x78\x1e\x78\x3c\x3c\x3c\x3c\x3c\x3c\x3c\x3c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x3c\x3c\x3c\x3c\x3c\x3c\x3c\x3c\x3c\x3c\x3c\x3c\x3c\x3c\x3c\x3c\x1e\x78\x1e\x78\x0f\xf0\x0f\xf0\x07\xe0\x07\xe0\x03\xc0\x03\xc0\x03\xc0\x03\xc0\x03\xc0\x03\xc0\x0f\xf0\x0f\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x3f\xfc\x3f\xfc\x38\x3c\x38\x3c\x30\x78\x30\x78\x00\xf0\x00\xf0\x01\xe0\x01\xe0\x03\xc0\x03\xc0\x07\x80\x07\x80\x0f\x00\x0f\x00\x1e\x0c\x1e\x0c\x3c\x1c\x3c\x1c\x3f\xfc\x3f\xfc\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0f\xf0\x0f\xf0\x0f\x00\x0f\x00\x0f\x00\x0f\x00\x0f\x00\x0f\x00\x0f\x00\x0f\x00\x0f\x00\x0f\x00\x0f\x00\x0f\x00\x0f\x00\x0f\x00\x0f\x00\x0f\x00\x0f\x00\x0f\x00\x0f\xf0\x0f\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x3c\x00\x3c\x00\x1e\x00\x1e\x00\x0f\x00\x0f\x00\x07\x80\x07\x80\x03\xc0\x03\xc0\x01\xe0\x01\xe0\x00\xf0\x00\xf0\x00\x78\x00\x78\x00\x3c\x00\x3c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0f\xf0\x0f\xf0\x00\xf0\x00\xf0\x00\xf0\x00\xf0\x00\xf0\x00\xf0\x00\xf0\x00\xf0\x00\xf0\x00\xf0\x00\xf0\x00\xf0\x00\xf0\x00\xf0\x00\xf0\x00\xf0\x00\xf0\x00\xf0\x0f\xf0\x0f\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x03\xc0\x03\xc0\x07\xe0\x07\xe0\x0f\xf0\x0f\xf0\x1e\x78\x1e\x78\x3c\x3c\x3c\x3c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x7f\xff\x7f\xff\x00\x00\x00\x00'\
b'\x03\xc0\x03\xc0\x03\xc0\x03\xc0\x01\xe0\x01\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\xe0\x0f\xe0\x00\x78\x00\x78\x0f\xf8\x0f\xf8\x3c\x78\x3c\x78\x3c\x78\x3c\x78\x3c\x78\x3c\x78\x0f\x9e\x0f\x9e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x3f\x00\x3f\x00\x0f\x00\x0f\x00\x0f\x00\x0f\x00\x0f\x00\x0f\x00\x0f\xf0\x0f\xf0\x0f\x3c\x0f\x3c\x0f\x1e\x0f\x1e\x0f\x1e\x0f\x1e\x0f\x1e\x0f\x1e\x0f\x1e\x0f\x1e\x3c\xf8\x3c\xf8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\xf8\x0f\xf8\x3c\x1e\x3c\x1e\x3c\x00\x3c\x00\x3c\x00\x3c\x00\x3c\x00\x3c\x00\x3c\x1e\x3c\x1e\x0f\xf8\x0f\xf8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x01\xf8\x01\xf8\x00\x78\x00\x78\x00\x78\x00\x78\x00\x78\x00\x78\x07\xf8\x07\xf8\x1e\x78\x1e\x78\x3c\x78\x3c\x78\x3c\x78\x3c\x78\x3c\x78\x3c\x78\x3c\x78\x3c\x78\x0f\x9e\x0f\x9e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\xf8\x0f\xf8\x3c\x1e\x3c\x1e\x3c\x1e\x3c\x1e\x3f\xfe\x3f\xfe\x3c\x00\x3c\x00\x3c\x1e\x3c\x1e\x0f\xf8\x0f\xf8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x03\xf0\x03\xf0\x0f\x3c\x0f\x3c\x0f\x0c\x0f\x0c\x0f\x00\x0f\x00\x0f\x00\x0f\x00\x3f\xf0\x3f\xf0\x0f\x00\x0f\x00\x0f\x00\x0f\x00\x0f\x00\x0f\x00\x0f\x00\x0f\x00\x3f\xc0\x3f\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\x9e\x0f\x9e\x3c\x78\x3c\x78\x3c\x78\x3c\x78\x3c\x78\x3c\x78\x3c\x78\x3c\x78\x0f\xf8\x0f\xf8\x00\x78\x00\x78\x3c\x78\x3c\x78\x0f\xe0\x0f\xe0\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x3f\x00\x3f\x00\x0f\x00\x0f\x00\x0f\x00\x0f\x00\x0f\x00\x0f\x00\x0f\x78\x0f\x78\x0f\x9e\x0f\x9e\x0f\x1e\x0f\x1e\x0f\x1e\x0f\x1e\x0f\x1e\x0f\x1e\x0f\x1e\x0f\x1e\x3f\x1e\x3f\x1e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf0\x00\xf0\x00\xf0\x00\xf0\x00\x00\x00\x00\x03\xf0\x03\xf0\x00\xf0\x00\xf0\x00\xf0\x00\xf0\x00\xf0\x00\xf0\x00\xf0\x00\xf0\x00\xf0\x00\xf0\x03\xfc\x03\xfc\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x3c\x00\x3c\x00\x3c\x00\x3c\x00\x00\x00\x00\x00\xfc\x00\xfc\x00\x3c\x00\x3c\x00\x3c\x00\x3c\x00\x3c\x00\x3c\x00\x3c\x00\x3c\x00\x3c\x00\x3c\x3c\x3c\x3c\x3c\x1e\x78\x1e\x78\x07\xe0\x07\xe0\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x3f\x00\x3f\x00\x0f\x00\x0f\x00\x0f\x00\x0f\x00\x0f\x00\x0f\x00\x0f\x1e\x0f\x1e\x0f\x3c\x0f\x3c\x0f\x78\x0f\x78\x0f\xf0\x0f\xf0\x0f\x78\x0f\x78\x0f\x3c\x0f\x3c\x3f\x1e\x3f\x1e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x03\xf0\x03\xf0\x00\xf0\x00\xf0\x00\xf0\x00\xf0\x00\xf0\x00\xf0\x00\xf0\x00\xf0\x00\xf0\x00\xf0\x00\xf0\x00\xf0\x00\xf0\x00\xf0\x00\xf0\x00\xf0\x00\xf0\x00\xf0\x03\xfc\x03\xfc\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x7e\x7c\x7e\x7c\x7f\xfe\x7f\xfe\x7b\xde\x7b\xde\x7b\xde\x7b\xde\x7b\xde\x7b\xde\x7b\xde\x7b\xde\x7b\xde\x7b\xde\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x3c\xf8\x3c\xf8\x0f\x3c\x0f\x3c\x0f\x1e\x0f\x1e\x0f\x1e\x0f\x1e\x0f\x1e\x0f\x1e\x0f\x1e\x0f\x1e\x0f\x1e\x0f\x1e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\xf0\x07\xf0\x1e\x3c\x1e\x3c\x3c\x1e\x3c\x1e\x3c\x1e\x3c\x1e\x3c\x1e\x3c\x1e\x1e\x3c\x1e\x3c\x07\xf0\x07\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x3c\xf0\x3c\xf0\x0f\x3c\x0f\x3c\x0f\x1e\x0f\x1e\x0f\x1e\x0f\x1e\x0f\x3c\x0f\x3c\x0f\xf0\x0f\xf0\x0f\x00\x0f\x00\x0f\x00\x0f\x00\x3f\xc0\x3f\xc0\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x9e\x07\x9e\x1e\x78\x1e\x78\x3c\x78\x3c\x78\x3c\x78\x3c\x78\x1e\x78\x1e\x78\x07\xf8\x07\xf8\x00\x78\x00\x78\x00\x78\x00\x78\x00\xfe\x00\xfe\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x3c\xf8\x3c\xf8\x0f\x9e\x0f\x9e\x0f\x00\x0f\x00\x0f\x00\x0f\x00\x0f\x00\x0f\x00\x0f\x00\x0f\x00\x3f\xc0\x3f\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\xf8\x0f\xf8\x3c\x1e\x3c\x1e\x3c\x00\x3c\x00\x0f\xf8\x0f\xf8\x00\x1e\x00\x1e\x3c\x1e\x3c\x1e\x0f\xf8\x0f\xf8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x01\x80\x01\x80\x03\x80\x03\x80\x07\x80\x07\x80\x07\x80\x07\x80\x7f\xf8\x7f\xf8\x07\x80\x07\x80\x07\x80\x07\x80\x07\x80\x07\x80\x07\x80\x07\x80\x07\x9e\x07\x9e\x01\xf8\x01\xf8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x3c\x78\x3c\x78\x3c\x78\x3c\x78\x3c\x78\x3c\x78\x3c\x78\x3c\x78\x3c\x78\x3c\x78\x3c\x78\x3c\x78\x0f\x9e\x0f\x9e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x78\x1e\x78\x1e\x78\x1e\x78\x1e\x78\x1e\x78\x1e\x78\x1e\x78\x1e\x1e\x78\x1e\x78\x07\xe0\x07\xe0\x01\x80\x01\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x78\x1e\x78\x1e\x78\x1e\x78\x1e\x78\x1e\x78\x1e\x79\x9e\x79\x9e\x7b\xde\x7b\xde\x3f\xfc\x3f\xfc\x1e\x78\x1e\x78\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x3c\x3c\x3c\x3c\x0e\x70\x0e\x70\x07\xe0\x07\xe0\x03\xc0\x03\xc0\x07\xe0\x07\xe0\x0e\x70\x0e\x70\x3c\x3c\x3c\x3c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x3c\x1e\x3c\x1e\x3c\x1e\x3c\x1e\x3c\x1e\x3c\x1e\x3c\x1e\x3c\x1e\x1e\x1e\x1e\x1e\x07\xfe\x07\xfe\x00\x1e\x00\x1e\x00\x3c\x00\x3c\x0f\xf0\x0f\xf0\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x3f\xfc\x3f\xfc\x3c\x3c\x3c\x3c\x00\xf0\x00\xf0\x03\xc0\x03\xc0\x0f\x00\x0f\x00\x3c\x3c\x3c\x3c\x3f\xfc\x3f\xfc\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\xfc\x00\xfc\x01\xe0\x01\xe0\x03\xc0\x03\xc0\x03\xc0\x03\xc0\x03\xc0\x03\xc0\x3f\x80\x3f\x80\x03\xc0\x03\xc0\x03\xc0\x03\xc0\x03\xc0\x03\xc0\x01\xe0\x01\xe0\x00\xfc\x00\xfc\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x03\xc0\x03\xc0\x03\xc0\x03\xc0\x03\xc0\x03\xc0\x03\xc0\x03\xc0\x03\xc0\x03\xc0\x00\x00\x00\x00\x03\xc0\x03\xc0\x03\xc0\x03\xc0\x03\xc0\x03\xc0\x03\xc0\x03\xc0\x03\xc0\x03\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x3f\x00\x3f\x00\x07\x80\x07\x80\x03\xc0\x03\xc0\x03\xc0\x03\xc0\x03\xc0\x03\xc0\x01\xfc\x01\xfc\x03\xc0\x03\xc0\x03\xc0\x03\xc0\x03\xc0\x03\xc0\x07\x80\x07\x80\x3f\x00\x3f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0f\x9e\x0f\x9e\x3c\xf8\x3c\xf8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc0\x00\xc0\x03\xf0\x03\xf0\x0f\x3c\x0f\x3c\x3c\x0f\x3c\x0f\x3c\x0f\x3c\x0f\x3f\xff\x3f\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\

FONT = memoryview(_FONT)
