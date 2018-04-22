import mock
from mock import call

from download.cmd.copy import Copy
from download.inputs.http_input import HttpInput
from download.inputs.input import Input
from download.outputs.file_output import FileOutput
from download.outputs.output import Output


def test_copy_reads_from_input_and_writes_to_output():
    input = mock.create_autospec(Input)
    input.read.side_effect = ('data1', 'data2', '')
    output = mock.create_autospec(Output)
    copy = Copy(input, output)
    copy.execute()
    input.read.assert_called()
    output.write.assert_has_calls([call('data1'), call('data2')])


def test_copy():
    def get_resource_name(src_url):
        return src_url.split('/')[-1]

    src_url = 'http://www.veneta-travel.com/uploads/hotels/hotel_1157/hotel_573341_stambolli2017.jpg'
    dst_path = './{}'.format(get_resource_name(src_url))
    input = HttpInput(src_url)
    output = FileOutput(dst_path)
    copy = Copy(input, output)
    copy.execute()
