import random

# Sample log templates
log_templates = [
    "[NEW] tcp 6 120 SYN_SENT src=10.1.2.3 dst={dst_ip1} sport=47800 dport=21 [UNREPLIED] src=203.0.113.47 dst={dst_ip2} sport=21 dport=47800 helper=ftp",
    "[UPDATE] tcp 6 60 SYN_RECV src=10.1.2.3 dst={dst_ip1} sport=47800 dport=21 src=203.0.113.47 dst={dst_ip2} sport=21 dport=47800 helper=ftp",
    "[UPDATE] tcp 6 432000 ESTABLISHED src=10.1.2.3 dst={dst_ip1} sport=47800 dport=21 src=203.0.113.47 dst={dst_ip2} sport=21 dport=47800 [ASSURED] helper=ftp",
]

def generate_random_log_entry():
    log_template = random.choice(log_templates)
    dst_ip1 = f"{random.randint(1, 5)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"
    dst_ip2 = f"{random.randint(1, 5)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"
    log_entry = log_template.format(dst_ip1=dst_ip1, dst_ip2=dst_ip2)
    return log_entry

def write_log_entries_to_file(num_entries=1000, file_name="generated_records.txt"):
    with open(file_name, "a") as file:
        for i in range(num_entries):
            log_entry = generate_random_log_entry()
            file.write(log_entry + "\n")

if __name__ == '__main__':
    write_log_entries_to_file()
