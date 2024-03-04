Digital Ocean API - CRUD for tags

```bash
Last login: Mon Mar  4 10:26:01 on ttys000
daniellopez@Daniels-MacBook-Air digital_ocean_api % ls
token.txt
daniellopez@Daniels-MacBook-Air digital_ocean_api % DIGITALOCEAN_TOKEN=$(cat token.txt)
daniellopez@Daniels-MacBook-Air digital_ocean_api % curl -X GET \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $DIGITALOCEAN_TOKEN" \
  "https://api.digitalocean.com/v2/tags"
{"tags":[],"links":{},"meta":{"total":0}}
daniellopez@Daniels-MacBook-Air digital_ocean_api % curl -X POST \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $DIGITALOCEAN_TOKEN" \
  -d '{"name":"awesome"}' \
  "https://api.digitalocean.com/v2/tags"
{"tag":{"name":"awesome","resources":{"count":0,"droplets":{"count":0},"images":{"count":0},"volumes":{"count":0},"volume_snapshots":{"count":0},"databases":{"count":0}}}}
daniellopez@Daniels-MacBook-Air digital_ocean_api % curl -X GET \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $DIGITALOCEAN_TOKEN" \
  "https://api.digitalocean.com/v2/tags/awesome"
{"tag":{"name":"awesome","resources":{"count":0,"droplets":{"count":0},"images":{"count":0},"volumes":{"count":0},"volume_snapshots":{"count":0},"databases":{"count":0}}}}
daniellopez@Daniels-MacBook-Air digital_ocean_api % curl -X DELETE \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $DIGITALOCEAN_TOKEN" \
  "https://api.digitalocean.com/v2/tags/awesome"
daniellopez@Daniels-MacBook-Air digital_ocean_api % curl -X GET \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $DIGITALOCEAN_TOKEN" \
  "https://api.digitalocean.com/v2/tags"
{"tags":[],"links":{},"meta":{"total":0}}
daniellopez@Daniels-MacBook-Air digital_ocean_api % 
```
