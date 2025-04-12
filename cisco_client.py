from netmiko import ConnectHandler

class CiscoDevice:
    def __init__(self, host):
        self.connection = ConnectHandler(
            device_type='cisco_ios',
            host=host,
            username='api_user',
            password='Secure123'
        )
    
    def get_cpu(self):
        return self.connection.send_command("show processes cpu sorted")
