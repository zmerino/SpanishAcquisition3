import random

from ...mock.mock_abstract_device import MockAbstractDevice
from ..voltagesource230 import voltageSource230

"""
Mock Sample ABC1234
"""


class MockvoltageSource230(MockAbstractDevice, voltageSource230):
	"""
	Mock interface for the Sample ABC1234.
	"""

	def __init__(self, *args, **kwargs):
		self.mocking = voltageSource230

		MockAbstractDevice.__init__(self, *args, **kwargs)

	def _reset(self):
		self.mock_state['setting'] = 'default value'

	def write(self, message, result=None, done=False):
		if not done:
			cmd, args, query = self._split_message(message)

			if cmd[0] == 'some':
				if cmd[1] == 'setting':
					if query:
						result = self.mock_state['setting']
					else:
						self.mock_state['setting'] = args
					done = True
			elif cmd[0] == 'read' and query:
				result = '-1.{0:04d}0000E-02'.format(random.randint(0, 9999))
				done = True

		MockAbstractDevice.write(self, message, result, done)


name = '230 Programmable Voltage Source'
implementation = MockvoltageSource230
