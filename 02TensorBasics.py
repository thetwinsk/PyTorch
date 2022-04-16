import torch
#x = torch.ones(2, 2, dtype=torch.int)
#print(x.dtype)
#print(x.size())

#x = torch.tensor([2.5, 0.1])

# x = torch.rand(2, 2)
# y = torch.rand(2, 2)
#print(x)

#z = x + y
# z = torch.add(x, y)

# y.add_(x)
# print(y)

# z = x - y
# z = torch.sub(x, y)

# z = x * y
# z = torch.mul(x, y)

# y.mul_(x)
# print(y)

# z = x / y
# z = torch.div(x, y)
# print(z)


# x = torch.rand(5, 3)
# print(x[:, 0])
# print(x[1, :])
# print(x[1, 1].item())

# x = torch.rand(4, 4)
# print(x)
# y = x.view(16)
# y = x.view(-1, 8)
# print(y)
# print(y.size())

import numpy as np
# a = torch.ones(5)
# print(a)
# b = a.numpy()
# print(type(b))
#be careful, just only use in CPU not GPU

# a = np.ones(5)
# print(a)
# b = torch.from_numpy(a)
# print(b)
#
# a += 1
# print(a)
# print(b) #be careful!

# if torch.cuda.is_available():
#     device = torch.device("cuda")
#     x = torch.ones(5, device=device)
#     y = torch.ones(5)
#     y = y.to(device)
#     z = x + y
#     z = z.to("cpu")

x = torch.ones(5, requires_grad=True)
print(x)












