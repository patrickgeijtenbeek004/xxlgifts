# ChatGPT Ads-feed Keycords & Lanyards

Elke dag om 06:17 (zomertijd) uploadt GitHub de feed in `feeds/` via SFTP naar ChatGPT Ads. OpenAI haalt zelf niets op en bewaart een product maximaal 14 dagen na de laatste upload.

## Nog in te stellen
Settings > Secrets and variables > Actions > New repository secret. Vul de gegevens in uit ChatGPT Ads Manager (Tools > Feeds):
- `SFTP_HOST`
- `SFTP_PORT`
- `SFTP_USER`
- `SFTP_PASSWORD`

Test daarna via Actions > "ChatGPT Ads feed uploaden" > Run workflow.

## Feed aanpassen
Vervang `feeds/keycords-lanyards_chatgpt_product_feed_keycords.csv` door een nieuwe versie met dezelfde naam. De upload start dan meteen. Voor elke upload controleert `scripts/check_feed.py` de feed; bij een fout gaat er niets naar OpenAI en krijg je een mail van GitHub.
