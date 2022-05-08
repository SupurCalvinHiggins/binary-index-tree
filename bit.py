class BinaryIndexTree:
	def __init__(self, max_idx):
		self.max_idx = max_idx
		self.bit_max_idx = self.max_idx + 1
		self.bit = [0] * (self.bit_max_idx + 1)

	def update(self, idx, val):
		if not 0 <= idx <= self.max_idx:
			raise IndexError("BinaryIndexTree index out of range")
		idx += 1

		while idx <= self.bit_max_idx:
			self.bit[idx] += val
			idx += (idx & -idx)

	def count_le(self, idx):
		if not 0 <= idx <= self.max_idx:
			raise IndexError("BinaryIndexTree index out of range")
		idx += 1

		total = 0
		while idx:
			total += self.bit[idx]
			idx -= (idx & -idx)
		return total

	def count_lt(self, idx):
		if not 0 <= idx <= self.max_idx:
			raise IndexError("BinaryIndexTree index out of range")

		if idx == 0:
			return 0
		return self.count_le(idx - 1)

	def count_ge(self, idx):
		if not 0 <= idx <= self.max_idx:
			raise IndexError("BinaryIndexTree index out of range")

		if idx == 0:
			return self.count_le(self.max_idx)
		return self.count_gt(idx - 1)

	def count_gt(self, idx):
		if not 0 <= idx <= self.max_idx:
			raise IndexError("BinaryIndexTree index out of range")

		return self.count_le(self.max_idx) - self.count_le(idx)

	def count_eq(self, idx):
		if not 0 <= idx <= self.max_idx:
			raise IndexError("BinaryIndexTree index out of range")

		return self.count_le(idx) - self.count_lt(idx)
