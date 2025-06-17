# test-universal-config

```bash
├── ...
├── configurations/
│   ├── base/
│   │      ├── aws-credentials.properties
│   │      └── microprofile-config-data-lineage.properties
│   ├── ci/
│   │      ├── aws-credentials.properties
│   │      └── microprofile-config-data-lineage.properties
│   ├── pom.xml
│   └── README.md
├── ...
├── pom.xml
└── README.md
```

```yaml
services:
  api:
    image: "test-4236-backend:0.0.1-SNAPSHOT"
    ports:
      - 8000:80
    volumes:
      - ./backend/src/test_4236_1/configurations:/tmp/configurations
    environment:
      - KRAUSENING_BASE=/tmp/configurations/base
      - KRAUSENING_EXTENSIONS=/tmp/configurations/ci
```

1. Create a simple repo contains reader class that can read property value with groupId and key ref: 
2. Create a loader class which can load the properties into environment variables
3. Create an easy script for user to encrypt the password ref: [Krausening Encryption](https://github.com/TechnologyBrewery/krausening/tree/dev/krausening#krausening-in-four-pints-leveraging-jasypt-for-encryptingdecrypting-properties)
4. Documentation
5. Simple example module to demo the usage