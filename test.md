**How to urlencode**

  To urlencode a string, we need to use _urllib.parse_ module in python 3( ** Not tested in Python 2 ** ).Here is an example:

```python
$ python3
>>> import urllib.parse
>>> jp = "Windows 8 で、コマンドプロンプトの起動方法が知りたい"
>>> jp_url = urllib.parse.quote_plus(jp)
>>> jp_url
'Windows+8+%E3%81%A7%E3%80%81%E3%82%B3%E3%83%9E%E3%83%B3%E3%83%89%E3%83%97%E3%83%AD%E3%83%B3%E3%83%97%E3%83%88%E3%81%AE%E8%B5%B7%E5%8B%95%E6%96%B9%E6%B3%95%E3%81%8C%E7%9F%A5%E3%82%8A%E3%81%9F%E3%81%84'
```


```json
  {
    'query': ['Windows 2000 に、ターミナルサービスクライアントをインストールしたい', 'Windows 2000 Server で、ユーザが ActiveDirectory にログオンできなくなった'],
    'true_answer_id': ['14638', '32602'],
    'first_response_id': ['14638', '32602'],
    'first_response_text': ['[Windows 2000] ターミナルサービスクライアントをインストールする方法', '[Windows 2000 Server] ユーザがActiveDirectoryにログオンできなくなった'],
    'second_response_id': ['14638', '32602'],
    'second_response_text': [' NT Workstation 4.0<br>Microsoft Windows ME<br>Microsoft Windows 98<br>Microsoft Windows 95<br><br>[処置]<br>ターミナルサービスを使用するには、以下の手順でクライアント（接続する側）にターミナルサービスクライアントをインストールする必要があります。<BR>ターミナルサービスクライアントの', '[情報]<br>Microsoft Windows 2000<br><br>[症状]<br>ユーザーがActiveDirectoryにログオンできなくなった。<br><br>[原因]<br>該当のユーザはパスワードなしであったが、「パスワードを無期限にする」にチェックがついていなかった。<BR>このため、ActiveDirectoryのアカウントポリシーパスワードの有効期間の設定が有効となり'],
    'third_response_id': ['36427', '171384'],
    'third_response_text': ['［Windows］ターミナルサービスクライアントでのショートカット', 'Windows 2000/Windows XP Users権限ユーザの省電力設定が正しく反映されない\u3000\u3000Windows2000/WindowsXPにて、Users権限でログオンしたユーザで、モニタの電源を切る設定をデフォルトの「20分」から「なし」に設定しても、ユーザが使用中に20分で切れてしまう。また、同一機種できちんと設定できている(モニタが切れない)ものもある。\u3000なぜこの様なことが起こるのか？']
  }
  ```