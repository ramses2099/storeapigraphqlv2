from flask import Flask, request, jsonify, render_template
from typing import Optional
from db import init_db



init_db()