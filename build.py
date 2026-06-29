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
        "badges": [
            "![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)",
            "![Rust](https://img.shields.io/badge/rust-%23000000.svg?style=for-the-badge&logo=rust&logoColor=white)",
            "![Cpp](https://img.shields.io/badge/c%2B%2B-%2300599C.svg?style=for-the-badge&logo=c%2B%2B&logoColor=white)",
            "![Shell Script](https://img.shields.io/badge/shell_script-%23121011.svg?style=for-the-badge&logo=gnu-bash&logoColor=white)",
            "![Vagrant](https://img.shields.io/badge/vagrant-%231563FF.svg?style=for-the-badge&logo=vagrant&logoColor=white)",
            "![Packer](https://img.shields.io/badge/packer-%23E7EEF0.svg?style=for-the-badge&logo=packer&logoColor=%2302A8EF)",
            "![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)",
            "![Kubernetes](https://img.shields.io/badge/kubernetes-%23326ce5.svg?style=for-the-badge&logo=kubernetes&logoColor=white)",
            "![Prometheus](https://img.shields.io/badge/Prometheus-E6522C?style=for-the-badge&logo=Prometheus&logoColor=white)",
            "![Grafana](https://img.shields.io/badge/grafana-%23F46800.svg?style=for-the-badge&logo=grafana&logoColor=white)",
            "![Ansible](https://img.shields.io/badge/ansible-%231A1918.svg?style=for-the-badge&logo=ansible&logoColor=white)",
            "![Markdown](https://img.shields.io/badge/markdown-%23000000.svg?style=for-the-badge&logo=markdown&logoColor=white)",
            "![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)",
            "![Redis](https://img.shields.io/badge/redis-%23DD0031.svg?style=for-the-badge&logo=redis&logoColor=white)",
            "![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)",
            "![AWS](https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white)",
            "![Azure](https://img.shields.io/badge/Azure-%230072C6.svg?style=for-the-badge&logo=microsoft-azure&logoColor=white)",
            "![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)",
            "![GitLab](https://img.shields.io/badge/gitlab-%23181717.svg?style=for-the-badge&logo=gitlab&logoColor=white)",
            "![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)",
            "![GitHub Actions](https://img.shields.io/badge/github%20actions-%232671E5.svg?style=for-the-badge&logo=githubactions&logoColor=white)",
            "![GitLab CI](https://img.shields.io/badge/gitlab%20ci-%23181717.svg?style=for-the-badge&logo=gitlab&logoColor=white)",
            "![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)",
            "![Debian](https://img.shields.io/badge/Debian-D70A53?style=for-the-badge&logo=debian&logoColor=white)",
            "![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)",
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
