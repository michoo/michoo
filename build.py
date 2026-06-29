#!/usr/bin/env python3
from profile_readme import get_github_context, ProfileGenerator


if __name__ == "__main__":
    context = {
        "linkedin": {
            "url": "https://www.linkedin.com/in/frederic-lopes-cyber/",
            "badge": "![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)",
        },
        "sds": [
            "![SD-Gitleaks](https://img.shields.io/badge/sd-gitleaks-brightgreen?style=for-the-badge)",
            "![SD-Titus](https://img.shields.io/badge/sd-titus-brightgreen?style=for-the-badge)"
        ],
        "scas": [
            
            "![SCA-Trivy](https://img.shields.io/badge/sca-trivy-brightgreen?style=for-the-badge)",
            "![SCA-Snyk](https://img.shields.io/badge/sca-snyk-brightgreen?style=for-the-badge)",
            "![SCA-OSV](https://img.shields.io/badge/sca-osv_scanner-brightgreen?style=for-the-badge)",
            "![SCA-SBOM](https://img.shields.io/badge/sca-sbom-brightgreen?style=for-the-badge)",
            "![SCA-Licenses](https://img.shields.io/badge/sca-licenses-brightgreen?style=for-the-badge)"
        ],
        "sasts": [
           
            "![SAST-Opengrep](https://img.shields.io/badge/sast-opengrep-brightgreen?style=for-the-badge)",
            "![SAST-Codeql](https://img.shields.io/badge/sast-codeql-brightgreen?style=for-the-badge)",
            "![SAST-Sonarqube](https://img.shields.io/badge/sast-sonarqube-brightgreen?style=for-the-badge)"
        ],
        "dasts": [
            "![DAST-Nuclei](https://img.shields.io/badge/dast-nuclei-brightgreen?style=for-the-badge)",
            "![DAST-Zaproxy](https://img.shields.io/badge/dast-zaproxy-brightgreen?style=for-the-badge)"
        ],
        "links": [
            {
                "title": "My blog",
                "link": "https://blog.kubeek.com"
            },
            {
                "title": "My more serious projects",
                "link": "https://github.com/kubeek-sec/"
            },
        ],
        "trainings": [
            {
                "title": "OSCP",
                "link": "https://github.com/michoo/sec-learning"
            },
        ]
    }
    context.update(**get_github_context("michoo"))
    ProfileGenerator.render(
        template_path="README-TEMPLATE.j2",
        output_path="README.md",
        context=context,
    )
