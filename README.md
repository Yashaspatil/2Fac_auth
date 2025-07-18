# 🔐 OTP Login System with Twilio

This is a simple Python-based login system that first validates a static password, then sends a One-Time Password (OTP) via SMS using the [Twilio API](https://www.twilio.com/) for a second layer of authentication.

## 📋 Features

- Static password verification
- OTP generation (6-digit random number)
- SMS-based OTP delivery using Twilio
- Maximum 5 password attempts
- Basic error handling for OTP delivery and input

## 🚀 Getting Started

### Prerequisites

- Python 3.x installed
- Twilio account with verified phone number
- Twilio Python helper library: Install it via pip

