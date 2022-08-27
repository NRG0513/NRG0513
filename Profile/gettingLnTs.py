from matplotlib.pyplot import figure, imshow, axis
from matplotlib.image import imread
from IPython.display import clear_output

compiledText = []

def gettingLnTs():
    listOfImgData =  [["code.visualstudio.com", "vscode-original", "vscode"],
                      ["jupyter.org", "jupyter-original-wordmark", "jupyter"],
                      ["www.python.org", "python-original", "python"],
                      ["www.gnu.org/software/bash", "bash-original", "bash"],
                      ["git-scm.com", "git-original", "git"],
                      ["github.com", "github-original", "github"],
                      ["numpy.org", "numpy-original", "numpy"],
                      ["www.tensorflow.org", "tensorflow-original", "tensorflow"],
                      ["pytorch.org", "pytorch-original", "pytorch"]]
    
    for i in range(0, len(listOfImgData)):
        
        htmlCode = f"https://raw.githubusercontent.com/NRG0513/NRG0513/main/Images/png/{listOfImgData[i][1]}.png"
        
        compiledText.append(htmlCode)
    
    clear_output(wait=True)
    return compiledText