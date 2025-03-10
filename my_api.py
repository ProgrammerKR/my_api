from flask import Flask, jsonify
import random

app = Flask(__name__)

# Extended list of 300 quotes
QUOTES = [
    "The greatest glory in living lies not in never falling, but in rising every time we fall. - Nelson Mandela",
    "The purpose of our lives is to be happy. - Dalai Lama",
    "Life is what happens when you're busy making other plans. - John Lennon",
    "Get busy living or get busy dying. - Stephen King",
    "You only live once, but if you do it right, once is enough. - Mae West",
    "In three words I can sum up everything I've learned about life: it goes on. - Robert Frost",
    "Life is really simple, but we insist on making it complicated. - Confucius",
    "To be yourself in a world that is constantly trying to make you something else is the greatest accomplishment. - Ralph Waldo Emerson",
    "Life is short, and it's up to you to make it sweet. - Sarah Louise Delany",
    "The way I see it, if you want the rainbow, you gotta put up with the rain. - Dolly Parton",
    "We do not remember days, we remember moments. - Cesare Pavese",
    "The only impossible journey is the one you never begin. - Tony Robbins",
    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
    "You must be the change you wish to see in the world. - Mahatma Gandhi",
    "To live is the rarest thing in the world. Most people exist, that is all. - Oscar Wilde",
    "You have within you right now, everything you need to deal with whatever the world can throw at you. - Brian Tracy",
    "The best way to predict the future is to create it. - Peter Drucker",
    "Life is what happens when you're busy making other plans. - John Lennon",
    "The only limit to our realization of tomorrow is our doubts of today. - Franklin D. Roosevelt",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
    "Happiness is not something ready made. It comes from your own actions. - Dalai Lama",
    "Everything has beauty, but not everyone can see. - Confucius",
    "The purpose of our lives is to be happy. - Dalai Lama",
    "Life is either a daring adventure or nothing at all. - Helen Keller",
    "You only live once, but if you do it right, once is enough. - Mae West",
    "The greatest glory in living lies not in never falling, but in rising every time we fall. - Nelson Mandela",
    "In the end, it's not the years in your life that count. It's the life in your years. - Abraham Lincoln",
    "Life is short, and it's up to you to make it sweet. - Sarah Louise Delany",
    "The best way to find yourself is to lose yourself in the service of others. - Mahatma Gandhi",
    "Life is what happens when you're busy making other plans. - John Lennon",
    "The only impossible journey is the one you never begin. - Tony Robbins",
    "You must be the change you wish to see in the world. - Mahatma Gandhi",
    "We do not remember days, we remember moments. - Cesare Pavese",
    "The way I see it, if you want the rainbow, you gotta put up with the rain. - Dolly Parton",
    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
    "The only limit to our realization of tomorrow is our doubts of today. - Franklin D. Roosevelt",
    "The best way to predict your future is to create it. - Peter Drucker",
    "Happiness is not something ready made. It comes from your own actions. - Dalai Lama",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
    "The purpose of our lives is to be happy. - Dalai Lama",
    "Life is either a daring adventure or nothing at all. - Helen Keller",
    "You have within you right now, everything you need to deal with whatever the world can throw at you. - Brian Tracy",
    "In the end, it's not the years in your life that count. It's the life in your years. - Abraham Lincoln",
    "The best way to find yourself is to lose yourself in the service of others. - Mahatma Gandhi",
    "Life is short, and it's up to you to make it sweet. - Sarah Louise Delany",
    "The way I see it, if you want the rainbow, you gotta put up with the rain. - Dolly Parton",
    "The only impossible journey is the one you never begin. - Tony Robbins",
    "You must be the change you wish to see in the world. - Mahatma Gandhi",
    "We do not remember days, we remember moments. - Cesare Pavese",
    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
    "The only limit to our realization of tomorrow is our doubts of today. - Franklin D. Roosevelt",
    "The best way to predict your future is to create it. - Peter Drucker",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
    "Happiness is not something ready made. It comes from your own actions. - Dalai Lama",
    "Life is what happens when you're busy making other plans. - John Lennon",
    "You only live once, but if you do it right, once is enough. - Mae West",
    "In three words I can sum up everything I've learned about life: it goes on. - Robert Frost",
    "Life is really simple, but we insist on making it complicated. - Confucius",
    "To be yourself in a world that is constantly trying to make you something else is the greatest accomplishment. - Ralph Waldo Emerson",
    "Life is short, and it's up to you to make it sweet. - Sarah Louise Delany",
    "The way I see it, if you want the rainbow, you gotta put up with the rain. - Dolly Parton",
    "We do not remember days, we remember moments. - Cesare Pavese",
    "The only impossible journey is the one you never begin. - Tony Robbins",
    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
    "You must be the change you wish to see in the world. - Mahatma Gandhi",
    "To live is the rarest thing in the world. Most people exist, that is all. - Oscar Wilde",
    "You have within you right now, everything you need to deal with whatever the world can throw at you. - Brian Tracy",
    "The best way to predict the future is to create it. - Peter Drucker",
    "Life is what happens when you're busy making other plans. - John Lennon",
    "The only limit to our realization of tomorrow is our doubts of today. - Franklin D. Roosevelt",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
    "Happiness is not something ready made. It comes from your own actions. - Dalai Lama",
    "Everything has beauty, but not everyone can see. - Confucius",
    "The purpose of our lives is to be happy. - Dalai Lama",
    "Life is either a daring adventure or nothing at all. - Helen Keller",
    "You only live once, but if you do it right, once is enough. - Mae West",
    "The greatest glory in living lies not in never falling, but in rising every time we fall. - Nelson Mandela",
    "In the end, it's not the years in your life that count. It's the life in your years. - Abraham Lincoln",
    "Life is short, and it's up to you to make it sweet. - Sarah Louise Delany",
    "The best way to find yourself is to lose yourself in the service of others. - Mahatma Gandhi",
    "Life is what happens when you're busy making other plans. - John Lennon",
    "The only impossible journey is the one you never begin. - Tony Robbins",
    "You must be the change you wish to see in the world. - Mahatma Gandhi",
    "We do not remember days, we remember moments. - Cesare Pavese",
    "The way I see it, if you want the rainbow, you gotta put up with the rain. - Dolly Parton",
    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
    "The only limit to our realization of tomorrow is our doubts of today. - Franklin D. Roosevelt",
    "The best way to predict your future is to create it. - Peter Drucker",
    "Happiness is not something ready made. It comes from your own actions. - Dalai Lama",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
    "The purpose of our lives is to be happy. - Dalai Lama",
    "Life is either a daring adventure or nothing at all. - Helen Keller",
    "You have within you right now, everything you need to deal with whatever the world can throw at you. - Brian Tracy",
    "In the end, it's not the years in your life that count. It's the life in your years. - Abraham Lincoln",
    "The best way to find yourself is to lose yourself in the service of others. - Mahatma Gandhi",
    "Life is short, and it's up to you to make it sweet. - Sarah Louise Delany",
    "The way I see it, if you want the rainbow, you gotta put up with the rain. - Dolly Parton",
    "The only impossible journey is the one you never begin. - Tony Robbins",
    "You must be the change you wish to see in the world. - Mahatma Gandhi",
    "We do not remember days, we remember moments. - Cesare Pavese",
    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
    "The only limit to our realization of tomorrow is our doubts of today. - Franklin D. Roosevelt",
    "The best way to predict your future is to create it. - Peter Drucker",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
    "Happiness is not something ready made. It comes from your own actions. - Dalai Lama",
    "Life is what happens when you're busy making other plans. - John Lennon",
    "You only live once, but if you do it right, once is enough. - Mae West",
    "In three words I can sum up everything I've learned about life: it goes on. - Robert Frost",
    "Life is really simple, but we insist on making it complicated. - Confucius",
    "To be yourself in a world that is constantly trying to make you something else is the greatest accomplishment. - Ralph Waldo Emerson",
    "Life is short, and it's up to you to make it sweet. - Sarah Louise Delany",
    "The way I see it, if you want the rainbow, you gotta put up with the rain. - Dolly Parton",
    "We do not remember days, we remember moments. - Cesare Pavese",
    "The only impossible journey is the one you never begin. - Tony Robbins",
    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
    "You must be the change you wish to see in the world. - Mahatma Gandhi",
    "To live is the rarest thing in the world. Most people exist, that is all. - Oscar Wilde",
    "You have within you right now, everything you need to deal with whatever the world can throw at you. - Brian Tracy",
    "The best way to predict the future is to create it. - Peter Drucker",
    "Life is what happens when you're busy making other plans. - John Lennon",
    "The only limit to our realization of tomorrow is our doubts of today. - Franklin D. Roosevelt",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
    "Happiness is not something ready made. It comes from your own actions. - Dalai Lama",
    "Everything has beauty, but not everyone can see. - Confucius",
    "The purpose of our lives is to be happy. - Dalai Lama",
    "Life is either a daring adventure or nothing at all. - Helen Keller",
    "You only live once, but if you do it right, once is enough. - Mae West",
    "The greatest glory in living lies not in never falling, but in rising every time we fall. - Nelson Mandela",
    "In the end, it's not the years in your life that count. It's the life in your years. - Abraham Lincoln",
    "Life is short, and it's up to you to make it sweet. - Sarah Louise Delany",
    "The best way to find yourself is to lose yourself in the service of others. - Mahatma Gandhi",
    "Life is what happens when you're busy making other plans. - John Lennon",
    "The only impossible journey is the one you never begin. - Tony Robbins",
    "You must be the change you wish to see in the world. - Mahatma Gandhi",
    "We do not remember days, we remember moments. - Cesare Pavese",
    "The way I see it, if you want the rainbow, you gotta put up with the rain. - Dolly Parton",
    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
    "The only limit to our realization of tomorrow is our doubts of today. - Franklin D. Roosevelt",
    "The best way to predict your future is to create it. - Peter Drucker",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
    "Happiness is not something ready made. It comes from your own actions. - Dalai Lama",
    "Life is what happens when you're busy making other plans. - John Lennon",
    "You only live once, but if you do it right, once is enough. - Mae West",
    "In three words I can sum up everything I've learned about life: it goes on. - Robert Frost",
    "Life is really simple, but we insist on making it complicated. - Confucius",
    "To be yourself in a world that is constantly trying to make you something else is the greatest accomplishment. - Ralph Waldo Emerson",
    "Life is short, and it's up to you to make it sweet. - Sarah Louise Delany",
    "The way I see it, if you want the rainbow, you gotta put up with the rain. - Dolly Parton",
    "We do not remember days, we remember moments. - Cesare Pavese",
    "The only impossible journey is the one you never begin. - Tony Robbins",
    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
    "You must be the change you wish to see in the world. - Mahatma Gandhi",
    "To live is the rarest thing in the world. Most people exist, that is all. - Oscar Wilde",
    "You have within you right now, everything you need to deal with whatever the world can throw at you. - Brian Tracy",
    "The best way to predict the future is to create it. - Peter Drucker",
    "Life is what happens when you're busy making other plans. - John Lennon",
    "The only limit to our realization of tomorrow is our doubts of today. - Franklin D. Roosevelt",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
    "Happiness is not something ready made. It comes from your own actions. - Dalai Lama",
    "Everything has beauty, but not everyone can see. - Confucius",
    "The purpose of our lives is to be happy. - Dalai Lama",
    "Life is either a daring adventure or nothing at all. - Helen Keller",
    "You only live once, but if you do it right, once is enough. - Mae West",
    "The greatest glory in living lies not in never falling, but in rising every time we fall. - Nelson Mandela",
    "In the end, it's not the years in your life that count. It's the life in your years. - Abraham Lincoln",
    "Life is short, and it's up to you to make it sweet. - Sarah Louise Delany",
    "The best way to find yourself is to lose yourself in the service of others. - Mahatma Gandhi",
    "Life is what happens when you're busy making other plans. - John Lennon",
    "The only impossible journey is the one you never begin. - Tony Robbins",
    "You must be the change you wish to see in the world. - Mahatma Gandhi",
    "We do not remember days, we remember moments. - Cesare Pavese",
    "The way I see it, if you want the rainbow, you gotta put up with the rain. - Dolly Parton",
    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
    "The only limit to our realization of tomorrow is our doubts of today. - Franklin D. Roosevelt",
    "The best way to predict your future is to create it. - Peter Drucker",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
    "Happiness is not something ready made. It comes from your own actions. - Dalai Lama",
    "Life is what happens when you're busy making other plans. - John Lennon",
    "You only live once, but if you do it right, once is enough. - Mae West",
    "In three words I can sum up everything I've learned about life: it goes on. - Robert Frost",
    "Life is really simple, but we insist on making it complicated. - Confucius",
    "To be yourself in a world that is constantly trying to make you something else is the greatest accomplishment. - Ralph Waldo Emerson",
    "Life is short, and it's up to you to make it sweet. - Sarah Louise Delany",
    "The way I see it, if you want the rainbow, you gotta put up with the rain. - Dolly Parton",
    "We do not remember days, we remember moments. - Cesare Pavese",
    "The only impossible journey is the one you never begin. - Tony Robbins",
    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
    "You must be the change you wish to see in the world. - Mahatma Gandhi",
    "To live is the rarest thing in the world. Most people exist, that is all. - Oscar Wilde",
    "You have within you right now, everything you need to deal with whatever the world can throw at you. - Brian Tracy",
    "The best way to predict the future is to create it. - Peter Drucker",
    "Life is what happens when you're busy making other plans. - John Lennon",
    "The only limit to our realization of tomorrow is our doubts of today. - Franklin D. Roosevelt",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
    "Happiness is not something ready made. It comes from your own actions. - Dalai Lama",
    "Everything has beauty, but not everyone can see. - Confucius",
    "The purpose of our lives is to be happy. - Dalai Lama",
    "Life is either a daring adventure or nothing at all. - Helen Keller",
    "You only live once, but if you do it right, once is enough. - Mae West",
    "The greatest glory in living lies not in never falling, but in rising every time we fall. - Nelson Mandela",
    "In the end, it's not the years in your life that count. It's the life in your years. - Abraham Lincoln",
    "Life is short, and it's up to you to make it sweet. - Sarah Louise Delany",
    "The best way to find yourself is to lose yourself in the service of others. - Mahatma Gandhi",
    "Life is what happens when you're busy making other plans. - John Lennon",
    "The only impossible journey is the one you never begin. - Tony Robbins",
    "You must be the change you wish to see in the world. - Mahatma Gandhi",
    "We do not remember days, we remember moments. - Cesare Pavese",
    "The way I see it, if you want the rainbow, you gotta put up with the rain. - Dolly Parton",
    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
    "The only limit to our realization of tomorrow is our doubts of today. - Franklin D. Roosevelt",
    "The best way to predict your future is to create it. - Peter Drucker",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
    "Happiness is not something ready made. It comes from your own actions. - Dalai Lama",
    "Life is what happens when you're busy making other plans. - John Lennon",
    "You only live once, but if you do it right, once is enough. - Mae West",
    "In three words I can sum up everything I've learned about life: it goes on. - Robert Frost",
    "Life is really simple, but we insist on making it complicated. - Confucius",
    "To be yourself in a world that is constantly trying to make you something else is the greatest accomplishment. - Ralph Waldo Emerson",
    "Life is short, and it's up to you to make it sweet. - Sarah Louise Delany",
    "The way I see it, if you want the rainbow, you gotta put up with the rain. - Dolly Parton",
    "We do not remember days, we remember moments. - Cesare Pavese",
    "The only impossible journey is the one you never begin. - Tony Robbins",
    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
    "You must be the change you wish to see in the world. - Mahatma Gandhi",
    "To live is the rarest thing in the world. Most people exist, that is all. - Oscar Wilde",
    "You have within you right now, everything you need to deal with whatever the world can throw at you. - Brian Tracy",
    "The best way to predict the future is to create it. - Peter Drucker",
    "Life is what happens when you're busy making other plans. - John Lennon",
    "The only limit to our realization of tomorrow is our doubts of today. - Franklin D. Roosevelt",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
    "Happiness is not something ready made. It comes from your own actions. - Dalai Lama",
    "Everything has beauty, but not everyone can see. - Confucius",
    "The purpose of our lives is to be happy. - Dalai Lama",
    "Life is either a daring adventure or nothing at all. - Helen Keller",
    "You only live once, but if you do it right, once is enough. - Mae West",
    "The greatest glory in living lies not in never falling, but in rising every time we fall. - Nelson Mandela",
    "In the end, it's not the years in your life that count. It's the life in your years. - Abraham Lincoln",
    "Life is short, and it's up to you to make it sweet. - Sarah Louise Delany",
    "The best way to find yourself is to lose yourself in the service of others. - Mahatma Gandhi",
    "Life is what happens when you're busy making other plans. - John Lennon",
    "The only impossible journey is the one you never begin. - Tony Robbins",
    "You must be the change you wish to see in the world. - Mahatma Gandhi",
    "We do not remember days, we remember moments. - Cesare Pavese",
    "The way I see it, if you want the rainbow, you gotta put up with the rain. - Dolly Parton",
    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
    "The only limit to our realization of tomorrow is our doubts of today. - Franklin D. Roosevelt",
    "The best way to predict your future is to create it. - Peter Drucker",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
    "Happiness is not something ready made. It comes from your own actions. - Dalai Lama",
    "Life is what happens when you're busy making other plans. - John Lennon",
    "You only live once, but if you do it right, once is enough. - Mae West",
    "In three words I can sum up everything I've learned about life: it goes on. - Robert Frost",
    "Life is really simple, but we insist on making it complicated. - Confucius",
    "To be yourself in a world that is constantly trying to make you something else is the greatest accomplishment. - Ralph Waldo Emerson",
    "Life is short, and it's up to you to make it sweet. - Sarah Louise Delany",
    "The way I see it, if you want the rainbow, you gotta put up with the rain. - Dolly Parton",
    "We do not remember days, we remember moments. - Cesare Pavese",
    "The only impossible journey is the one you never begin. - Tony Robbins",
    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
    "You must be the change you wish to see in the world. - Mahatma Gandhi",
    "To live is the rarest thing in the world. Most people exist, that is all. - Oscar Wilde",
    "You have within you right now, everything you need to deal with whatever the world can throw at you. - Brian Tracy",
    "The best way to predict the future is to create it. - Peter Drucker",
    "Life is what happens when you're busy making other plans. - John Lennon",
    "The only limit to our realization of tomorrow is our doubts of today. - Franklin D. Roosevelt",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
    "Happiness is not something ready made. It comes from your own actions. - Dalai Lama",
    "Everything has beauty, but not everyone can see. - Confucius",
    "The purpose of our lives is to be happy. - Dalai Lama",
    "Life is either a daring adventure or nothing at all. - Helen Keller",
    "You only live once, but if you do it right, once is enough. - Mae West",
    "The greatest glory in living lies not in never falling, but in rising every time we fall. - Nelson Mandela",
    "In the end, it's not the years in your life that count. It's the life in your years. - Abraham Lincoln",
    "Life is short, and it's up to you to make it sweet. - Sarah Louise Delany",
    "The best way to find yourself is to lose yourself in the service of others. - Mahatma Gandhi",
    "Life is what happens when you're busy making other plans. - John Lennon",
    "The only impossible journey is the one you never begin. - Tony Robbins",
    "You must be the change you wish to see in the world. - Mahatma Gandhi",
    "We do not remember days, we remember moments. - Cesare Pavese",
    "The way I see it, if you want the rainbow, you gotta put up with the rain. - Dolly Parton",
    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
    "The only limit to our realization of tomorrow is our doubts of today. - Franklin D. Roosevelt",
    "The best way to predict your future is to create it. - Peter Drucker",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
    "Happiness is not something ready made. It comes from your own actions. - Dalai Lama",
    "Life is what happens when you're busy making other plans. - John Lennon",
    "You only live once, but if you do it right, once is enough. - Mae West",
    "In three words I can sum up everything I've learned about life: it goes on. - Robert Frost",
    "Life is really simple, but we insist on making it complicated. - Confucius",
    "To be yourself in a world that is constantly trying to make you something else is the greatest accomplishment. - Ralph Waldo Emerson",
    "Life is short, and it's up to you to make it sweet. - Sarah Louise Delany",
    "The way I see it, if you want the rainbow, you gotta put up with the rain. - Dolly Parton",
    "We do not remember days, we remember moments. - Cesare Pavese",
    "The only impossible journey is the one you never begin. - Tony Robbins",
    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
    "You must be the change you wish to see in the world. - Mahatma Gandhi",
    "To live is the rarest thing in the world. Most people exist, that is all. - Oscar Wilde",
    "You have within you right now, everything you need to deal with whatever the world can throw at you. - Brian Tracy",
    "The best way to predict the future is to create it. - Peter Drucker",
    "Life is what happens when you're busy making other plans. - John Lennon",
    "The only limit to our realization of tomorrow is our doubts of today. - Franklin D. Roosevelt",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
    "Happiness is not something ready made. It comes from your own actions. - Dalai Lama",
    "Everything has beauty, but not everyone can see. - Confucius",
    "The purpose of our lives is to be happy. - Dalai Lama",
    "Life is either a daring adventure or nothing at all. - Helen Keller",
    "You only live once, but if you do it right, once is enough. - Mae West",
    "The greatest glory in living lies not in never falling, but in rising every time we fall. - Nelson Mandela",
    "In the end, it's not the years in your life that count. It's the life in your years. - Abraham Lincoln",
    "Life is short, and it's up to you to make it sweet. - Sarah Louise Delany",
    "The best way to find yourself is to lose yourself in the service of others. - Mahatma Gandhi",
    "Life is what happens when you're busy making other plans. - John Lennon",
    "The only impossible journey is the one you never begin. - Tony Robbins",
    "You must be the change you wish to see in the world. - Mahatma Gandhi",
    "We do not remember days, we remember moments. - Cesare Pavese",
    "The way I see it, if you want the rainbow, you gotta put up with the rain. - Dolly Parton",
    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
    "The only limit to our realization of tomorrow is our doubts of today. - Franklin D. Roosevelt",
    "The best way to predict your future is to create it. - Peter Drucker",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
    "Happiness is not something ready made. It comes from your own actions. - Dalai Lama",
    "Life is what happens when you're busy making other plans. - John Lennon",
    "You only live once, but if you do it right, once is enough. - Mae West",
    "In three words I can sum up everything I've learned about life: it goes on. - Robert Frost",
    "Life is really simple, but we insist on making it complicated. - Confucius",
    "To be yourself in a world that is constantly trying to make you something else is the greatest accomplishment. - Ralph Waldo Emerson",
    "Life is short, and it's up to you to make it sweet. - Sarah Louise Delany",
    "The way I see it, if you want the rainbow, you gotta put up with the rain. - Dolly Parton",
    "We do not remember days, we remember moments. - Cesare Pavese",
    "The only impossible journey is the one you never begin. - Tony Robbins",
    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
    "You must be the change you wish to see in the world. - Mahatma Gandhi",
    "To live is the rarest thing in the world. Most people exist, that is all. - Oscar Wilde",
    "You have within you right now, everything you need to deal with whatever the world can throw at you. - Brian Tracy",
    "The best way to predict the future is to create it. - Peter Drucker",
    "Life is what happens when you're busy making other plans. - John Lennon",
    "The only limit to our realization of tomorrow is our doubts of today. - Franklin D. Roosevelt",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
    "Happiness is not something ready made. It comes from your own actions. - Dalai Lama",
    "Everything has beauty, but not everyone can see. - Confucius",
    "The purpose of our lives is to be happy. - Dalai Lama",
    "Life is either a daring adventure or nothing at all. - Helen Keller",
    "You only live once, but if you do it right, once is enough. - Mae West",
    "The greatest glory in living lies not in never falling, but in rising every time we fall. - Nelson Mandela",
    "In the end, it's not the years in your life that count. It's the life in your years. - Abraham Lincoln",
    "Life is short, and it's up to you to make it sweet. - Sarah Louise Delany",
    "The best way to find yourself is to lose yourself in the service of others. - Mahatma Gandhi",
    "Life is what happens when you're busy making other plans. - John Lennon",
    "The only impossible journey is the one you never begin. - Tony Robbins",
    "You must be the change you wish to see in the world. - Mahatma Gandhi",
    "We do not remember days, we remember moments. - Cesare Pavese",
    "The way I see it, if you want the rainbow, you gotta put up with the rain. - Dolly Parton",
    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
    "The only limit to our realization of tomorrow is our doubts of today. - Franklin D. Roosevelt",
    "The best way to predict your future is to create it. - Peter Drucker",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
    "Happiness is not something ready made. It comes from your own actions. - Dalai Lama",
    "Life is what happens when you're busy making other plans. - John Lennon",
    "You only live once, but if you do it right, once is enough. - Mae West",
    "In three words I can sum up everything I've learned about life: it goes on. - Robert Frost",
    "Life is really simple, but we insist on making it complicated. - Confucius",
    "To be yourself in a world that is constantly trying to make you something else is the greatest accomplishment. - Ralph Waldo Emerson",
    "Life is short, and it's up to you to make it sweet. - Sarah Louise Delany",
    "The way I see it, if you want the rainbow, you gotta put up with the rain. - Dolly Parton",
    "We do not remember days, we remember moments. - Cesare Pavese",
    "The only impossible journey is the one you never begin. - Tony Robbins",
    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
    "You must be the change you wish to see in the world. - Mahatma Gandhi",
    "To live is the rarest thing in the world. Most people exist, that is all. - Oscar Wilde",
    "You have within you right now, everything you need to deal with whatever the world can throw at you. - Brian Tracy",
    "The best way to predict the future is to create it. - Peter Drucker",
    "Life is what happens when you're busy making other plans. - John Lennon",
    "The only limit to our realization of tomorrow is our doubts of today. - Franklin D. Roosevelt",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
    "Happiness is not something ready made. It comes from your own actions. - Dalai Lama",
    "Everything has beauty, but not everyone can see. - Confucius",
    "The purpose of our lives is to be happy. - Dalai Lama",
    "Life is either a daring adventure or nothing at all. - Helen Keller",
    "You only live once, but if you do it right, once is enough. - Mae West",
    "The greatest glory in living lies not in never falling, but in rising every time we fall. - Nelson Mandela",
    "In the end, it's not the years in your life that count. It's the life in your years. - Abraham Lincoln",
    "Life is short, and it's up to you to make it sweet. - Sarah Louise Delany",
    "The best way to find yourself is to lose yourself in the service of others. - Mahatma Gandhi"
]

@app.route('/')
def home():
    return "Welcome to the Random Quote Generator."

@app.route('/api/quote', methods=['GET'])
def get_quote():
    quote = random.choice(QUOTES)
    return jsonify({"quote": quote})

if __name__ == '__main__':
    app.run(debug=True)
    