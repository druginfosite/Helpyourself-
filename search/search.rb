require 'open-uri'
require 'nokogiri'

def search(query)
  url = "https://www.google.com/search?q=#{query}"
  doc = Nokogiri::HTML(open(url))
  results = []
  doc.css('div.g').each do |result|
    link = result.css('a').first['href']
    title = result.css('h3').text
    item = {
      'title' => title,
      'link' => link
    }
    results << item
  end
  return results
end