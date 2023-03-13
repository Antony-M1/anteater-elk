After `clone` the project you have to run all the docker compose `up` or `stop` or `down` command in the `anteater-elk` folder or
where the `docker-compose.yml` file presented from there you have to run the command

For more reference
[YouTube Video](https://youtu.be/VpAH2IoMzKw)

**Step 1**

copy the `anteater.log` file from the log folder after that create a `temp` folder in from your `root` directory
after that past that log file inside the `temp` folder. the final file structure like this
`root/temp/anteater.log`

**Step 2**

run all the container to create the credentials to use this command
```
docker compose up
```
then access the `elasticsearch` container using this command
```
docker exec -it -u root elasticsearch bash
```
after that run this command, it will generate all the credentials `note: It won't appear next time so please note some where`,
incase you missed those credentials, this command won't work i will attach the command to change the password for a user
```
bin/elasticsearch-setup-passwords auto
```
then you have to create the `enrollment token` using this command. `note: it's only created by once so please note some where`.
this command also you have to run inside the `elasticsearch` conatiner
```
bin/elasticsearch-create-enrollment-token --scope kibana
```

**Step 3**

After creating all the neccessary credentials `stop` and `down` the containers. using this command.
if you run the setup in `detach` mode but we are not running in `detach` mode so can simply do
`Ctrl + c` in the terminal.
```
docker compose stop
```
after stoping the container remove it
```
docker compose down
```

**Step 4**

After change the credentials in the respective files are `kibana/kibana.yml`
```
elasticsearch.username: kibana_system
elasticsearch.password: <YOUR_KIBANA_SYSTEM_PASSWORD>
```
`logstash/logstash.conf`
```
output {
   elasticsearch {
       hosts => ["http://elasticsearch:9200"]
       user => "elastic"
       password => <YOUR_ELASTIC_PASSWORD>
   }
}
```
`logstash/logstash.yml`
```
xpack.monitoring.elasticsearch.username: elastic
xpack.monitoring.elasticsearch.password: <YOUR_ELASTIC_PASSWORD>
```

**Step 5**

Run the Project in detach mode using this command
```
docker compose up -d
```

then check this port `http://localhost:5601/` you can able to access the kibana and pass the enrollment token and other credentials

firewall
```
sudo firewall-cmd --add-port=9200/tcp --permanent
sudo firewall-cmd --add-port=5601/tcp --permanent
sudo firewall-cmd --add-port=9600/tcp --permanent
sudo firewall-cmd --add-port=9300/tcp --permanent
sudo firewall-cmd --reload
```


