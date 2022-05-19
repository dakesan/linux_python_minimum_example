import subprocess


# この引数の内容を変えて遊んでみましょう
arg1 = "aaaaaaaaaaaaaaaaa"
arg2 = "bbbbbbbbbbbbbbbbb"
# 実際に行われるコマンドは以下
ARG = "bash test.sh " + arg1 + " " + arg2

# 以下コマンドによりpythonからbashスクリプトを実行するプロセスが立ち上がります。
ps = subprocess.Popen(args=ARG, shell=True)

print(">>pythonからbashスクリプトを実行中・・・")
ps.wait()
print(">>pythonから実行完了を確認！ヨシ！")