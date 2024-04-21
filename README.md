# AWS IoT Certificates and Scripts

Welcome to the repository containing AWS IoT certificates and scripts for IoT device communication. This repository includes the following files:

---

## Certificate Files:

1. **AmazonRootCA1.pem**:
   - Description: Root CA certificate provided by Amazon for secure communication with AWS IoT.

2. **fc04d9accfe28c9f63616f9d8182730aff04cea5730ad16485a8716815bef08e-certificate.pem.crt**:
   - Description: Device certificate issued by AWS IoT for device authentication.

3. **fc04d9accfe28c9f63616f9d8182730aff04cea5730ad16485a8716815bef08e-private.pem.key**:
   - Description: Private key associated with the device certificate for secure communication.

4. **fc04d9accfe28c9f63616f9d8182730aff04cea5730ad16485a8716815bef08e-public.pem.key**:
   - Description: Public key associated with the device certificate for secure communication.

---

## Scripts:

1. **main.py**:
   - Description: Main script for implementing IoT device functionality. This script may include device initialization, sensor data collection, and communication with AWS IoT Core.

2. **sender_publisher.py**:
   - Description: Script for publishing messages to AWS IoT topics. This script may be used to send sensor data or control commands to other IoT devices or services.

3. **subscriber.py**:
   - Description: Script for subscribing to AWS IoT topics and receiving messages from other devices or services. This script may be used to monitor events or receive commands from other devices.

---

## Usage:

- Clone or download the repository to your development environment.
- Add the certificate files provided by AWS IoT to authenticate your device with AWS IoT Core.
- Modify the scripts according to your specific IoT application requirements.
- Run the scripts on your IoT devices to establish secure communication with AWS IoT Core and implement desired functionality.

---

## Contributing:

- Contributions to improve existing scripts or add new features are welcome. Please follow the contribution guidelines provided in the repository.

---

## License:

- This repository is provided under the [MIT License](https://opensource.org/licenses/MIT). Feel free to use and modify the scripts according to your needs.

---

Feel free to explore the repository and utilize the provided certificates and scripts for your AWS IoT projects. If you have any questions or feedback, don't hesitate to reach out.
