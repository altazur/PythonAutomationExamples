import requests
import xml.etree.ElementTree as ET

"""Class which contains xml requests builders and requests method to obtain response with result"""
class Calculator():
    
    ADD_METHOD_NAME = 'Add'

    def __prepare_xml_body(self, intA, intB, method, soap_version):
        xsi = "http://www.w3.org/2001/XMLSchema-instance"
        xsd = "http://www.w3.org/2001/XMLSchema"
        soap = "http://schemas.xmlsoap.org/soap/envelope/" if soap_version == '1.1' or "http://www.w3.org/2003/05/soap-envelope"
        xmlns = "http://tempuri.org/"
        soap_tag = 'soap' if soap_version == '1.1' or 'soap12'

        env_map = {'xsi': xsi, 'xsd': xsd}
        method_map = {None: xmlns}

        ET.register_namespace('xsi', xsi)
        ET.register_namespace('xsd', xsd)
        ET.register_namespace(soap_tag, soap)

        qname_env = ET.QName(soap, 'Envelope')
        qname_body = ET.QName(soap, 'Body')

        envelope = ET.Element(qname_env, nsmap=env_map)
        body = ET.SubElement(envelope, qname_body)
        operation = ET.SubElement(body, method, nsmap=method_map)
        int_a = ET.SubElement(operation, 'intA')
        int_b = ET.SubElement(operation, 'intB')
        int_a.text = str(intA)
        int_b.text = str(intB)
        
        return ET.tostring(envelope)

    def add(self, intA, intB, soap_version):
        """Return response from ADD endpoint"""
        body = self.__prepare_xml_body(intA, intB, self.ADD_METHOD_NAME, soap_version)
        headers = {'Content-Type': 'text/xml; charset=utf-8', 'Content-Length': str(len(body)), 'SOAPAction': f'http://tempuri.org/{self.ADD_METHOD_NAME}'} if soap_version == '1.1' or {'Content-Type': 'application/soap+xml; charset=utf-8', 'Content-Length': str(len(body))}
        response = requests.post(url='http://www.dneonline.com/calculator.asmx', headers=headers, data=body, verify=False)
        assert response.status_code == 200
        xml_response = ET.fromstring(response.content)
        return xml_response.findall('.//')[2].text
