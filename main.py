from common import utils

out, rc, err = utils.execute(['ls', '-la'])
print(out, rc, err)
