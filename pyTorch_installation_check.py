import torch

class CheckingInstallations:
    def __init__(self, check = None,cuda_check= None):
        self.pytorch_check = torch.__version__
        self.cuda_check = torch.cuda.is_available()
        

    def pytorch_installation_check(self):
        try:
            return f"PyTorch version installed in your project directory is: { self.pytorch_check}"
        except AttributeError:
            self.message = "PyTorch has not been installed properly. Make sure your python version is supported by PyTorch."
            return self.message


    def cuda_available_check(self):
        try:
            # print(f"CUDA TYPE:{type(cuda_check)}")
            if self.cuda_check:
                gpu_name = torch.cuda.get_device_name(0)
            return f"CUDA Available:{self.cuda_check}; GPU Name:{gpu_name}"
        except  AttributeError:
            self.message = "No CUDA is available."
            return self.message
        


def main():
    # making object of checkingInstallations class
    check_installations = CheckingInstallations()
    
    result_pytorch_installation = check_installations.pytorch_installation_check()
    print("CHECKING PYTORCH INSTALLATION")
    print(result_pytorch_installation)
    print("\n")
    result_cuda_available = check_installations.cuda_available_check()
    print("CHECKING CUDA Availability")
    print(f"{result_cuda_available}")


if __name__ == "__main__":
    main()