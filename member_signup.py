import subprocess
import logging

class MemberManager:
    def __init__(self):
        pass

    def add_member(self, email, role="member"):
        logging.info(f"Attempting to add {email} with role {role}")
        try:
            # Corrected the command based on the provided format
            cmd = f"cnvrgv2 members add --email='{email}' --role='{role}'"
            logging.info(f"Executing command: {cmd}")
            result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            if result.returncode == 0:
                return True
            else:
                logging.error(f"Failed to add {email}. Command failed with error: {result.stderr.strip()}")
                return False
        except Exception as e:
            logging.error(f"Error adding member {email}: {e}")
            return False

    def add_multiple_members(self, base_email_prefix, domain, start_index, end_index, role):
        for i in range(start_index, end_index + 1):
            email = f"{base_email_prefix}{i}@{domain}"
            success = self.add_member(email, role)
            if success:
                print(f"Successfully added {email} with role {role}")
            else:
                print(f"Failed to add {email} with role {role}")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    manager = MemberManager()
    manager.add_multiple_members(base_email_prefix="chen", domain="cnvrg.io", start_index=1, end_index=200, role="admin")
