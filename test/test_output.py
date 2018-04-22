from expects import expect, equal

from download.outputs.file_output import FileOutput


def test_file_output():
    path = './out.txt'
    out = FileOutput(path)
    out.open()
    data = 'foo bar'
    out.write(data)
    out.close()

    with open(path, 'r') as f:
        expect(f.read()).to(equal(data))
