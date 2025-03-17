import base64
import uuid
from cryptography.fernet import Fernet

# Provided encrypted string
encoded_string = "gAAAAABnbn8oO0O7Omqtqufcp6Nk5l4484KpgLs6aii8Kz2f_n2XP6Zb3IJfmxOO7iTu_AqYedOy9wpAKVOY5km7sqDJhTdzu2ZBldl8-vwunrvHaL602_ZOsON-koFbo9SUemw4scBmINBESZtjBBPycYIb6uuZ6aWQ70ywnsqYrn8Zyr5Fc2umRkaEghU5JS8eKxU9FA8KSZmMeqweClYM4mm4CyO3nzk7PHwht8usYSpKmNBrQccWCzvGCxFl4T_Q0tTJMk1JIQ_WWhJCcxQMeKMlBJV0oE0AoMd4Aw_o7B3QjTEQorI="
uuid_str = "afc01eea-8fce-4471-99a2-a0b46642fc7d"

try:
    # Decode Base64 string to bytes
    decoded_bytes = base64.b64decode(encoded_string)
    # Convert UUID to 16 bytes and double to 32 bytes
    uuid_bytes = uuid.UUID(uuid_str).bytes
    key = base64.urlsafe_b64encode(uuid_bytes * 2)
    # Initialize Fernet with the key
    f = Fernet(key)
    # Decrypt the message
    decrypted_message = f.decrypt(decoded_bytes)
    print("Decrypted Message:", decrypted_message.decode())
except Exception as e:
    print(f"Decryption failed: {e}")
