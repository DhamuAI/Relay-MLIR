
from tvm.driver import tvmc


model = tvmc.load("/home/dhamodharan-alphaics/Dhamodharan/llvm_test/Relay-MLIR/data/matmul.onnx")

print(model.summary())