
function pushd2() {
  PUSHED="$(pwd)"
  cd "$PROJDIR""$1" >>/dev/null
}

function popd2() {
  cd "${PUSHED:-"$PROJDIR"}" >>/dev/null
  unset PUSHED
}

showmigrations() {
  manage showmigrations $*
}

function makemigrations() {
  manage makemigrations $*
}

function migrate() {
  manage migrate $*
}

function djshell() {
  manage shell
}

function dbshell() {
  manage dbshell
}

function createsuperuser() {
  manage createsuperuser
}

function manage() {
  pushd2 /dj
  python manage.py $*
  r=$?
  popd2
  return ${r}
}

function recreatedb() {
  psql -h localhost -U template1 -c "CREATE USER root;"
  psql -h pg -U postgres -c "ALTER USER root WITH SUPERUSER;"
  psql -h pg -c "DROP DATABASE IF EXISTS order_mgmnt;" template1
  psql -h pg -c "CREATE DATABASE order_mgmnt" template1
  psql -h pg -c "CREATE EXTENSION IF NOT EXISTS hstore;" order_mgmnt
  psql -h pg -c "CREATE EXTENSION IF NOT EXISTS citext;" order_mgmnt
  psql -h pg -c "CREATE EXTENSION IF NOT EXISTS postgis;" order_mgmnt
  migrate $*
}

function pyfmt() {
  black $PROJDIR/dj
}
