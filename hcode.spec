{
  "name": "shell-zedboard-xillybus-ap_fifo32",
  "type": "shell",
  "version": "0.1.1",
  "summary": "An hCODE shell based on xillinux-eval-zedboard-1.3c module.",
  "description": "Developed in Computer Arch. Lab@Kumamoto University, Japan.",
  "homepage": "http://arch.cs.kumamoto-u.ac.jp/hcode",
  "license": "MIT",
  "authors": {
    "Qian ZHAO": "cho@arch.cs.kumamoto-u.ac.jp"
  },
  "source": {
    "git": "https://github.com/jonsonxp/shell-zedboard-xillybus-ap_fifo32.git",
    "tag": "0.1.1"
  },
  "hardware": {
    "board": "zedboard",
    "device": "xc7z020clg484-1"
  },
  "interface": {
    "host": {
      "ap_fifo": {
        "data_width": 32
       },
       "mem": {
        "data_width": 256
       } 
    }
  }
}
