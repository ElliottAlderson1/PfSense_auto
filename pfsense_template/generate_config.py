import xml.etree.ElementTree as ET
import yaml

def load_inventory(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

def generate_config(template_path, inventory, output_path):
    tree = ET.parse(template_path)
    root = tree.getroot()
    
    # Apply VLAN configurations
    vlans = inventory['vlans']
    for vlan in vlans:
        vlan_element = ET.Element('vlan')
        id_element = ET.SubElement(vlan_element, 'id')
        id_element.text = str(vlan['id'])
        name_element = ET.SubElement(vlan_element, 'name')
        name_element.text = vlan['name']
        ip_element = ET.SubElement(vlan_element, 'ip')
        ip_element.text = vlan['ip']
        root.find('vlans').append(vlan_element)
    
    # Apply Firewall rules
    firewall_rules = inventory['firewall_rules']
    for rule in firewall_rules:
        rule_element = ET.Element('rule')
        action_element = ET.SubElement(rule_element, 'action')
        action_element.text = rule['action']
        source_element = ET.SubElement(rule_element, 'source')
        source_element.text = rule['source']
        destination_element = ET.SubElement(rule_element, 'destination')
        destination_element.text = rule['destination']
        protocol_element = ET.SubElement(rule_element, 'protocol')
        protocol_element.text = rule['protocol']
        root.find('filter').append(rule_element)
    
    # Apply HA settings
    ha_element = root.find('hasync')
    ha_element.find('pfsyncinterface').text = inventory['ha']['pfsync_interface']
    ha_element.find('pfsyncpeerip').text = inventory['ha']['peer_ip']
    
    # Create new user
    new_user_element = ET.Element('user')
    name_element = ET.SubElement(new_user_element, 'name')
    name_element.text = inventory['new_user']['username']
    password_element = ET.SubElement(new_user_element, 'password')
    password_element.text = inventory['new_user']['password']
    root.find('system').append(new_user_element)
    
    # Set DHCP relay
    dhcp_relay_element = root.find('dhcpd').find('lan').find('failover_peerip')
    dhcp_relay_element.text = inventory['dhcp_relay']
    
    tree.write(output_path)

# Example usage
inventory_path = 'inventory.yaml'
template_path = '/c/Users/Ninja/Desktop/DevOps_1-24/Pfsense_project/auto-pfsense/pfsense.xml'  # Update this path
output_path = '/c/Users/Ninja/Desktop/DevOps_1-24/Pfsense_project/auto-pfsense/generated_config.xml'  # Update this path

inventory = load_inventory(inventory_path)
generate_config(template_path, inventory, output_path)
