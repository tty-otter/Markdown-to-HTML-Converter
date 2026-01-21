import sys
import os
import markdown

def main():
    if len(sys.argv) != 4 or sys.argv[1] != "markdown":
        show_usage()
        sys.exit(1)

    input_filepath = sys.argv[2]
    output_filepath = check_output_filepath(sys.argv[3])

    try:
        markdown.markdownFromFile(input=input_filepath, output=output_filepath, extensions=["tables"])
        print(f"処理が正常に完了。出力ファイルパス：{output_filepath}")
    except FileNotFoundError:
        print(f"無効な入力ファイルパスです。{input_filepath}が存在しません。")
    except Exception as e:
        print(f"エラーが発生。：{e}")

def show_usage():
    print("入力に誤りがあります。例を参考に入力してください。")
    print("python3 markdownToHTMLConverter.py markdown <input_filepath> <output_filepath>")

def check_output_filepath(output_filepath):
    try:
        with open(output_filepath, 'w') as f:
            f.write("Create for testing.")
        os.remove(output_filepath)
        return output_filepath
    except:
        # エラーが発生したばあいは同じフォルダにoutput.htmlで出力。
        return "output.html"

if __name__ == "__main__":
    main()
