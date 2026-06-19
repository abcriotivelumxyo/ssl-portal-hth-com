def load_site_data():
    return [
        {
            "url": "https://ssl-portal-hth.com",
            "keywords": ["hth", "portal", "ssl"],
            "tags": ["security", "authentication", "gateway"],
            "description": "SSL portal providing secure access and authentication gateway services.",
        },
        {
            "url": "https://example.org",
            "keywords": ["example", "demo"],
            "tags": ["sample", "reference"],
            "description": "A general example site for demonstration and testing.",
        },
    ]

def format_summary(entry):
    kw_str = ", ".join(entry["keywords"])
    tag_str = ", ".join(entry["tags"])
    lines = [
        f"URL: {entry['url']}",
        f"Keywords: {kw_str}",
        f"Tags: {tag_str}",
        f"Description: {entry['description']}",
    ]
    return "\n".join(lines)

def generate_summary(data):
    parts = []
    for i, entry in enumerate(data, start=1):
        parts.append(f"--- Site {i} ---")
        parts.append(format_summary(entry))
        parts.append("")
    return "\n".join(parts).strip()

def main():
    sites = load_site_data()
    summary = generate_summary(sites)
    print("Structured Site Summary")
    print("=" * 40)
    print(summary)

if __name__ == "__main__":
    main()