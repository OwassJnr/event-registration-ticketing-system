# Event Registration & Ticketing System

A serverless REST API built on AWS Cloud Services for managing event registrations and ticketing. The system replaces traditional Microsoft Forms and Excel-based workflows with a scalable, automated, and cost-effective cloud-native solution.

---

## Project Overview

This project provides a fully serverless backend that allows users to:

- View available events
- Register for events
- Retrieve registrations by email
- Cancel registrations

The solution leverages AWS managed services to achieve scalability, reliability, and low operational overhead.

---

## Architecture

### High-Level Architecture

GitHub Repository
↓
GitHub Actions (CI/CD)
↓
Amazon API Gateway
↓
AWS Lambda Functions
↓
Amazon DynamoDB

Supporting Services:

- Amazon CloudWatch (Monitoring & Logging)
- Amazon SNS (Notifications)
- AWS Budgets (Cost Monitoring)

---

## AWS Services Used

| Service | Purpose |
|----------|----------|
| AWS Lambda | Serverless business logic |
| Amazon API Gateway | REST API endpoints |
| Amazon DynamoDB | Data storage |
| Amazon SNS | Email notifications |
| Amazon CloudWatch | Logs, metrics, alarms |
| AWS Budgets | Cost monitoring |
| GitHub Actions | CI/CD automation |

---

## DynamoDB Tables

### Events Table

| Attribute | Type |
|------------|------|
| eventId | String (Partition Key) |
| name | String |
| date | String |
| capacity | Number |
| registeredCount | Number |

### Registration Table

| Attribute | Type |
|------------|------|
| registrationId | String (Partition Key) |
| eventId | String |
| name | String |
| email | String |
| timestamp | String |

### Global Secondary Index

| Index Name | Partition Key |
|------------|---------------|
| email-index | email |

---

## API Endpoints

### Get All Events

```http
GET /events
```

Response:

```json
[
  {
    "eventId": "EVT001",
    "name": "AWS Workshop Accra 2026"
  }
]
```

---

### Register for an Event

```http
POST /register
```

Request:

```json
{
  "eventId": "EVT001",
  "name": "John Doe",
  "email": "john@example.com"
}
```

Response:

```json
{
  "message": "Registration successful",
  "registrationId": "xxxxxxxx"
}
```

---

### View Registrations

```http
GET /registrations/{email}
```

Example:

```http
GET /registrations/john@example.com
```

Response:

```json
[
  {
    "registrationId": "xxxxxxxx",
    "eventId": "EVT001",
    "email": "john@example.com"
  }
]
```

---

### Cancel Registration

```http
DELETE /registration/{id}
```

Response:

```json
{
  "message": "Registration cancelled"
}
```

---

## CI/CD Pipeline

GitHub Actions is used to automate validation and quality checks.

### Workflow Features

- Automatic execution on push
- Automatic execution on pull requests
- Python environment setup
- Dependency installation
- Python syntax validation

Workflow file:

```text
.github/workflows/ci.yml
```

---

## Monitoring and Logging

### Amazon CloudWatch

CloudWatch is used for:

- Lambda execution logs
- Application logs
- Error tracking
- Alarm monitoring

### CloudWatch Alarm

Alarm Name:

```text
RegisterFunctionErrorAlarm
```

Purpose:

```text
Triggers when Lambda errors exceed the configured threshold.
```

---

## Notifications

Amazon SNS is used for email notifications.

Topic:

```text
EventRegistrationNotifications
```

Capabilities:

- Alarm notifications
- Registration notifications
- Operational alerts

---

## Cost Management

AWS Budgets is configured to monitor project spending.

Configuration:

- Monthly Budget: $5
- Alert Threshold: 80%

---

## Security

Security measures implemented:

- IAM Roles for Lambda execution
- API Gateway integration controls
- Input validation
- CloudWatch monitoring
- Principle of Least Privilege (documented)

Future enhancements:

- JWT Authentication
- API Keys
- AWS Cognito Integration

---

## Project Structure

```text
event-registration-ticketing-system/
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── src/
│   ├── getEvents/
│   ├── register/
│   ├── getRegistrations/
│   └── deleteRegistration/
│
├── template.yaml
├── requirements.txt
├── events.json
├── README.md
├── LICENSE
└── .gitignore
```

---

## Deployment

### Prerequisites

- AWS Account
- GitHub Account
- Python 3.11+
- VS Code

### Deployment Steps

1. Create DynamoDB tables
2. Create Lambda functions
3. Configure API Gateway
4. Configure IAM permissions
5. Deploy API
6. Configure SNS
7. Configure CloudWatch alarms
8. Configure AWS Budgets

---

## Challenges Encountered

During implementation, several challenges were addressed:

- Git merge conflicts during repository setup
- DynamoDB Decimal serialization issues
- API Gateway routing configuration
- Lambda IAM permissions
- DynamoDB table naming inconsistencies
- CloudWatch troubleshooting

---

## Future Improvements

Potential enhancements include:

- Frontend web application
- JWT authentication
- AWS Cognito integration
- Event capacity validation
- Email templates
- Infrastructure as Code deployment
- Automated testing framework

---

## Author

Owass Jnr

---

## License

This project is licensed under the MIT License.