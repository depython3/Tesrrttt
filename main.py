import flet as ft
import os
import sys
import base64
import random
import zipfile
import shutil
import tempfile
import subprocess
import uuid
import datetime
import threading

def main(page: ft.Page):
    # إعدادات الصفحة
    page.title = "NinjiGramPro Encryptor"
    page.theme_mode = ft.ThemeMode.DARK
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.scroll = ft.ScrollMode.AUTO
    page.padding = 20

    # متغيرات حالة
    selected_file = None
    protection_type = "expiry"
    expiry_date = None
    username = None
    server_url = None
    user_id = None
    user_token = None

    # عناصر واجهة المستخدم
    time_display = ft.Text("", size=18, color=ft.colors.CYAN)
    file_name_display = ft.Text("", color=ft.colors.WHITE)
    encrypt_btn = ft.ElevatedButton(
        "Encrypt Files",
        bgcolor=ft.colors.TEAL,
        color=ft.colors.WHITE,
        disabled=True,
        on_click=lambda e: start_encryption()
    )
    message_display = ft.Text("", color=ft.colors.GREEN)
    error_display = ft.Text("", color=ft.colors.RED)

    # وظائف مساعدة
    def update_time():
        now = datetime.datetime.now()
        time_display.value = now.strftime("%H:%M:%S")
        page.update()

    def install():
        try:
            import cython
            print('# - Cython is already installed')
        except ImportError:
            print('# - Installing cython...')
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'cython'])
            import cython

    def xor_base64_enc(data: str, key: list) -> str:
        return ''.join([chr(ord(c) ^ key[i % len(key)]) for i, c in enumerate(data)])

    def enc_line(lines, keys):
        lll = []
        for line in lines:
            line = line.rstrip('\n')
            s1 = xor_base64_enc(line, keys['key1'])
            s2 = xor_base64_enc(s1, keys['key2'])
            b64_encoded = base64.b64encode(s2.encode()).decode()
            lll.append(b64_encoded)
        return lll

    def enc(lll, keys, user_id, user_token):
        return f'''
import base64

def ll(data: str, key: list) -> str:
    return ''.join([chr(ord(c) ^ key[i % len(key)]) for i, c in enumerate(data)])

def run(lll, keys):
    l = []
    for enc in lll:
        s = base64.b64decode(enc).decode()
        s = ll(s, keys["key2"])
        s = ll(s, keys["key1"])
        l.append(s)
    return "\\n".join(l)

# User credentials
ID = "{user_id}"
Token = "{user_token}"

lll = {repr(lll)}
keys = {{"key1": {keys["key1"]},"key2": {keys["key2"]}}}

code = run(lll, keys)
exec(code)
'''

    def add_expiry_check(code, expiry_date, username):
        expiry_code = f"""
import os
import datetime
now = datetime.date.today()
target = datetime.date({expiry_date.year}, {expiry_date.month}, {expiry_date.day})
if now >= target:
    exit(f" - Turn Off This Tool ... ! Please Wait For {username}")
"""
        return expiry_code + "\n" + code

    def add_server_check(code, server_url):
        server_code = f"""
Server = None
try:
    Check_Server = __import__('requests').get('{server_url}').text
    if 'ON' in Check_Server:
        Server = True
        print("✓ Server Status: Active")
    else:
        print("✗ Server Status: Offline")
        print(f'- Turn Off This Tool ... ! Please Wait For -')
        exit()
except:
    print("✗ Server Status: Connection Failed")
    print(f'- Turn Off This Tool ... ! Please Wait For -')
    exit()
"""
        return server_code + "\n" + code

    def elf(source_path, working_dir, protection_type, user_id, user_token, expiry_date=None, username=None, server_url=None):
        install()
        keys = {
            'key1': [57, 86, 161, 120, 219, 27, 229, 199, 203, 14, 186, 181, 233, 27, 149, 196, 69, 19, 179, 3, 74, 180, 28, 108, 120, 218, 130, 20, 162, 9, 28, 239, 229, 177, 215],
            'key2': [89, 112, 199, 20, 188, 180, 138, 41, 94, 79, 150, 166, 144, 246, 180, 42, 219, 68, 26, 40, 38, 192, 98, 98, 145, 219, 199, 162, 183, 97, 104, 101, 197, 164, 59, 251, 64, 108, 103, 139]
        }

        with open(source_path, 'r', encoding='utf-8', errors='ignore') as f:
            original_code = f.read()
        
        # Add protection based on selected type
        if protection_type == 'expiry':
            if not expiry_date or not username:
                raise Exception("Expiry date and username are required for expiry protection")
            modified_code = add_expiry_check(original_code, expiry_date, username)
        elif protection_type == 'server':
            if not server_url:
                raise Exception("Server URL is required for server protection")
            modified_code = add_server_check(original_code, server_url)
        else:
            modified_code = original_code
        
        # Write modified code to temporary file
        modified_path = os.path.join(working_dir, 'modified_input.py')
        with open(modified_path, 'w', encoding='utf-8') as f:
            f.write(modified_code)
        
        # Process the modified file
        with open(modified_path, 'r', encoding='utf-8', errors='ignore') as f:
            lines = f.readlines()

        lll = enc_line(lines, keys)
        final_code = enc(lll, keys, user_id, user_token)
        
        r = """
# - Enc : Plya_Team - BY - LAEGER_MO OR @sis_c   
__J=''
__C=chr
import zipfile as I,os as o,shutil as K,tempfile as T,sys as s,platform as M,subprocess as P
def NinjramPro():
 A=o.path.dirname(o.path.abspath(s.argv[0]));B=T.mkdtemp();
 try:
  C=o.path.abspath(s.argv[0]);
  with I.ZipFile(C,(__J.join(__C(c^106) for c in [24])))as D:D.extractall(B);
  E=M.machine();F={(__J.join(__C(c^16) for c in [81, 93, 84, 38, 36])):(__J.join(__C(c^242) for c in [188, 155, 156, 152, 128, 147, 159, 162, 128, 157, 196, 198])),(__J.join(__C(c^161) for c in [217, 153, 151, 254, 151, 149])):(__J.join(__C(c^189) for c in [243, 212, 211, 215, 207, 220, 208, 237, 207, 210, 139, 137])),(__J.join(__C(c^207) for c in [174, 174, 189, 172, 167, 249, 251])):(__J.join(__C(c^12) for c in [66, 101, 98, 102, 126, 109, 97, 92, 126, 99, 58, 56])),(__J.join(__C(c^207) for c in [174, 189, 162, 185, 248, 163])):(__J.join(__C(c^114) for c in [60, 27, 28, 24, 0, 19, 31, 34, 0, 29, 65, 64])),(__J.join(__C(c^86) for c in [55, 36, 59, 32, 110, 58])):(__J.join(__C(c^124) for c in [50, 21, 18, 22, 14, 29, 17, 44, 14, 19, 79, 78])),(__J.join(__C(c^10) for c in [107, 120, 103, 60, 62])):(__J.join(__C(c^12) for c in [66, 101, 98, 102, 126, 109, 97, 92, 126, 99, 58, 56])),(__J.join(__C(c^186) for c in [194, 130, 140])):(__J.join(__C(c^30) for c in [80, 119, 112, 116, 108, 127, 115, 78, 108, 113, 45, 44])),(__J.join(__C(c^29) for c in [116, 46, 37, 43])):(__J.join(__C(c^92) for c in [18, 53, 50, 54, 46, 61, 49, 12, 46, 51, 111, 110])),(__J.join(__C(c^207) for c in [166, 249, 247, 249])):(__J.join(__C(c^209) for c in [159, 184, 191, 187, 163, 176, 188, 129, 163, 190, 226, 227]))};
  if E not in F:print(f"Unsupported machine architecture: {E}");s.exit(1);
  G=F[E];H=o.path.join(B,G);
  if not o.path.exists(H):print(f"Binary not found for architecture: {E} at path: {H}");s.exit(1);
  o.chmod(H,0o755);o.chdir(A);P.run([H]+s.argv[1:]);
 except I.BadZipFile:print((__J.join(__C(c^130) for c in [199, 240, 240, 237, 240, 184, 162, 214, 234, 235, 241, 162, 231, 250, 231, 225, 247, 246, 227, 224, 238, 231, 162, 235, 241, 162, 236, 237, 246, 162, 227, 162, 244, 227, 238, 235, 230, 162, 216, 203, 210, 162, 228, 235, 238, 231, 162, 237, 240, 162, 235, 241, 162, 225, 237, 240, 240, 247, 242, 246, 231, 230, 172])));
 except Exception as J:print(f"An error occurred: {J}");
 finally:
  try:K.rmtree(B);
  except Exception as L:print(f"Warning: Could not remove temporary directory: {L}");

if __name__==(__J.join(__C(c^60) for c in [99, 99, 81, 93, 85, 82, 99, 99])):NinjramPro();
    """

        o_py_path = os.path.join(working_dir, "oo.py")
        c_path = os.path.join(working_dir, "NinjcythonPro.c")
        main_py_path = os.path.join(working_dir, '__main__.py')
        bin32 = os.path.join(working_dir, "NinjramPro32")
        bin64 = os.path.join(working_dir, "NinjramPro64")

        with open(o_py_path, "w", encoding='utf-8') as f:
            f.write(final_code)

        try:
            subprocess.run(['cython', '--embed', '-3', '--directive', 'annotation_typing=False', '-o', c_path, o_py_path], check=True)
            subprocess.run(['gcc', '-w', '-m32', c_path, '-o', bin32, '-fvisibility=hidden', '-s', '-fno-stack-protector', 
                          '-fPIE', '-pie', '-fomit-frame-pointer', '-Wl,-z,relro,-z,now', '-Wl,-s'] + 
                          subprocess.check_output(['python3-config', '--cflags', '--ldflags']).decode().split(), check=True)
        except subprocess.CalledProcessError as e:
            raise Exception(f"Compilation failed: {e}")

        with open(main_py_path, 'w', encoding='utf-8') as run_elf:
            run_elf.write(r)

        zip_file = os.path.join(working_dir, '.NinjiGramPro')
        with zipfile.ZipFile(zip_file, 'w', zipfile.ZIP_DEFLATED) as zipf:
            zipf.write(main_py_path, arcname='__main__.py')
            zipf.write(bin32, arcname='NinjramPro32')

        with open(zip_file,'rb') as file_base64:
            read_file = file_base64.read()
        base64_src = base64.b64encode(read_file).decode()

        NinjiGramPro = f'''
import os, sys, base64 as B
A = '.NinjiGramPro'
C = {base64_src!r}
try:
    with open(A,'wb')as D:D.write(B.b64decode(C))
    os.system('python3 .NinjiGramPro '+' '.join(sys.argv[1:]))
except Exception as E:print(E)
finally:
    if os.path.exists(A):os.remove(A)
'''

        # Save to /sdcard/ENC_Plya_Team
        storage_path = "/sdcard/ENC_Plya_Team"
        os.makedirs(storage_path, exist_ok=True)
        final_output = os.path.join(storage_path, 'Enc_NinjiGramPro.py')
        
        with open(final_output, 'w') as n:
            n.write(NinjiGramPro)

        return final_output

    def start_encryption():
        nonlocal selected_file, protection_type, user_id, user_token, expiry_date, username, server_url
        
        if not selected_file:
            error_display.value = "No file selected"
            error_display.visible = True
            message_display.visible = False
            page.update()
            return

        # الحصول على القيم من الحقول
        user_id = user_id_field.value
        user_token = user_token_field.value
        
        if not user_id or not user_token:
            error_display.value = "ID and Token are required"
            error_display.visible = True
            message_display.visible = False
            page.update()
            return

        # التحقق بناءً على نوع الحماية
        if protection_type == "expiry":
            expiry_date_str = expiry_date_field.value
            username = username_field.value
            
            if not expiry_date_str or not username:
                error_display.value = "Expiry date and username are required for expiry protection"
                error_display.visible = True
                message_display.visible = False
                page.update()
                return
                
            try:
                expiry_date = datetime.datetime.strptime(expiry_date_str, '%Y-%m-%d').date()
            except ValueError:
                error_display.value = "Invalid date format. Use YYYY-MM-DD"
                error_display.visible = True
                message_display.visible = False
                page.update()
                return
                
        elif protection_type == "server":
            server_url = server_url_field.value
            
            if not server_url:
                error_display.value = "Server URL is required for server protection"
                error_display.visible = True
                message_display.visible = False
                page.update()
                return

        # تعطيل الزر أثناء التشفير
        encrypt_btn.disabled = True
        encrypt_btn.text = "Encrypting..."
        message_display.value = "Encryption in progress..."
        message_display.visible = True
        error_display.visible = False
        page.update()

        # تشفير الملف في خيط منفصل
        def encryption_thread():
            try:
                # إنشاء مجلد مؤقت
                temp_dir = tempfile.mkdtemp()
                session_id = str(uuid.uuid4())
                working_dir = os.path.join(temp_dir, session_id)
                os.makedirs(working_dir, exist_ok=True)

                # حفظ الملف المرفوع
                source_path = os.path.join(working_dir, 'input.py')
                with open(source_path, 'wb') as f:
                    f.write(selected_file)

                result_file = elf(source_path, working_dir, protection_type, user_id, user_token, expiry_date, username, server_url)
                
                # تنظيف الملفات المؤقتة
                shutil.rmtree(temp_dir, ignore_errors=True)
                
                # عرض رسالة النجاح
                message_display.value = f"Done! File saved to: {result_file}"
                message_display.visible = True
                error_display.visible = False
                
            except Exception as e:
                error_display.value = f"Encryption failed: {str(e)}"
                error_display.visible = True
                message_display.visible = False
                
            finally:
                # إعادة تمكين الزر
                encrypt_btn.disabled = False
                encrypt_btn.text = "Encrypt Files"
                page.update()

        # تشغيل التشفير في خيط منفصل
        threading.Thread(target=encryption_thread).start()

    def file_picker_result(e: ft.FilePickerResultEvent):
        nonlocal selected_file
        if e.files:
            selected_file = e.files[0].read()
            file_name_display.value = f"Selected File: {e.files[0].name}"
            file_name_display.visible = True
            encrypt_btn.disabled = False
        else:
            selected_file = None
            file_name_display.value = ""
            file_name_display.visible = False
            encrypt_btn.disabled = True
        
        page.update()

    def protection_type_changed(e):
        nonlocal protection_type
        protection_type = e.control.value
        
        # إظهار/إخفاء الحقول بناءً على نوع الحماية
        expiry_section.visible = (protection_type == "expiry")
        server_section.visible = (protection_type == "server")
        page.update()

    # عناصر واجهة المستخدم
    file_picker = ft.FilePicker(on_result=file_picker_result)
    page.overlay.append(file_picker)

    # حقل اختيار الملف
    choose_file_btn = ft.ElevatedButton(
        "Choose Python File",
        icon=ft.icons.UPLOAD_FILE,
        on_click=lambda _: file_picker.pick_files(
            allowed_extensions=["py"], 
            allow_multiple=False
        )
    )

    # حقول الإدخال
    user_id_field = ft.TextField(
        label="Your ID",
        hint_text="Enter your ID",
        width=400
    )
    
    user_token_field = ft.TextField(
        label="Your Token",
        hint_text="Enter your token",
        width=400
    )

    # خيارات نوع الحماية
    protection_radio = ft.RadioGroup(
        content=ft.Column([
            ft.Radio(value="expiry", label="Expiry Date Protection"),
            ft.Radio(value="server", label="Server Check Protection")
        ]),
        value="expiry",
        on_change=protection_type_changed
    )

    # قسم تاريخ الانتهاء
    expiry_date_field = ft.TextField(
        label="Expiry Date (YYYY-MM-DD)",
        hint_text="2023-12-31",
        width=400
    )
    
    username_field = ft.TextField(
        label="Your Username",
        hint_text="@your_username",
        width=400
    )
    
    expiry_section = ft.Column([
        expiry_date_field,
        username_field,
        ft.Text("Tool will stop working after this date", size=12, color=ft.colors.GREY)
    ], visible=True)

    # قسم التحقق من الخادم
    server_url_field = ft.TextField(
        label="Server URL (for checking)",
        hint_text="https://example.com/status.txt",
        width=400
    )
    
    server_section = ft.Column([
        server_url_field,
        ft.Text("Tool will check this URL for 'ON' status", size=12, color=ft.colors.GREY)
    ], visible=False)

    # بناء واجهة المستخدم
    page.add(
        ft.Row([
            time_display,
            ft.Container(
                content=ft.Text("NinjiGramPro", size=24, weight=ft.FontWeight.BOLD,
                               gradient=ft.LinearGradient(
                                   begin=ft.alignment.top_left,
                                   end=ft.alignment.bottom_right,
                                   colors=[ft.colors.RED, ft.colors.WHITE, ft.colors.RED]
                               )),
                padding=10
            ),
            ft.IconButton(
                icon=ft.icons.ACCOUNT_CIRCLE,
                icon_size=40,
                on_click=lambda e: page.show_dialog(
                    ft.AlertDialog(
                        title=ft.Text("Encryption Information"),
                        content=ft.Column([
                            ft.Text("Advanced encryption system for Python files with multiple layers of protection."),
                            ft.Text("Support Team:", weight=ft.FontWeight.BOLD),
                            ft.Text("First supporter: @LAEGER_MO"),
                            ft.Text("Second supporter: @sis_c")
                        ], tight=True),
                        actions=[ft.TextButton("OK", on_click=lambda e: page.close_dialog())]
                    )
                )
            )
        ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
        
        ft.Container(
            content=ft.Column([
                ft.Text("Enc_NinjiGramPro By Plya_Team", size=20, weight=ft.FontWeight.BOLD),
                
                choose_file_btn,
                file_name_display,
                
                user_id_field,
                user_token_field,
                
                ft.Text("Protection Type:", weight=ft.FontWeight.BOLD),
                protection_radio,
                
                expiry_section,
                server_section,
                
                encrypt_btn,
                message_display,
                error_display,
                
                ft.Container(
                    content=ft.Column([
                        ft.Text("How to Use", size=16, weight=ft.FontWeight.BOLD, color=ft.colors.CYAN),
                        ft.Text("1. Click 'Choose Python File' to select your file"),
                        ft.Text("2. The file will be uploaded automatically"),
                        ft.Text("3. Click 'Encrypt Files' to start encryption process"),
                        ft.Text("4. Download your encrypted file when ready")
                    ]),
                    padding=10,
                    bgcolor=ft.colors.BLUE_GREY_900,
                    border_radius=10,
                    width=400
                ),
                
                ft.Container(
                    content=ft.Column([
                        ft.Text("Copyright & Credentials", size=16, weight=ft.FontWeight.BOLD, color=ft.colors.CYAN),
                        ft.Text("This software is developed by Plya_Team"),
                        ft.Text(f"User ID: {user_id_field.value or 'XXXXXX'}"),
                        ft.Text(f"Token: {'*' * 10}")
                    ]),
                    padding=10,
                    bgcolor=ft.colors.BLUE_GREY_900,
                    border_radius=10,
                    width=400
                )
            ], spacing=20, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            padding=20
        ),
        
        ft.FloatingActionButton(
            icon=ft.icons.ACCESS_TIME,
            on_click=lambda e: page.show_dialog(
                ft.AlertDialog(
                    title=ft.Text("Time Information"),
                    content=ft.Column([
                        ft.Text(f"Current Date: {datetime.datetime.now().strftime('%Y-%m-%d')}"),
                        ft.Text(f"Current Time: {datetime.datetime.now().strftime('%H:%M:%S')}"),
                        ft.Text("About Expiry System:", weight=ft.FontWeight.BOLD),
                        ft.Text("The tool will automatically stop working after the expiry date you set."),
                        ft.Text("When expired, it will show your username and stop execution.")
                    ], tight=True),
                    actions=[ft.TextButton("OK", on_click=lambda e: page.close_dialog())]
                )
            )
        )
    )

    # تحديث الوقت كل ثانية
    def update_time_loop():
        while True:
            update_time()
            import time
            time.sleep(1)

    threading.Thread(target=update_time_loop, daemon=True).start()

ft.app(target=main)
