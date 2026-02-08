from django.core.management.base import BaseCommand
from portfolio.models import PortfolioItem


class Command(BaseCommand):
    help = 'Seed the database with Ravi Rastogi portfolio data'

    def handle(self, *args, **options):
        # Clear existing data
        PortfolioItem.objects.all().delete()
        self.stdout.write('Cleared existing portfolio items...')

        items = [
            # Profile
            {
                'category': 'profile',
                'title': 'Ravi Rastogi',
                'subtitle': 'AI/ML Engineer & Full-Stack Developer',
                'description': '''
                    <p class="mb-2">📍 Dublin, Ireland</p>
                    <p class="mb-2">📧 itsravirastogi@gmail.com</p>
                    <p class="mb-2">📱 +353 89 956 4137</p>
                    
                    <p class="mt-4 leading-relaxed">
                        AI/ML Engineer pursuing an MSc at University College Dublin, specializing in NLP and climate research. 
                        Currently researching climate-induced migration detection using geospatial analysis and NLP under Prof. Elisa D'Amico. 
                        Published in Springer on computational emotion analysis, with proven expertise in LLM optimization (60% cost reduction), 
                        RAG architectures, and production ML systems. Combines technical skills with business impact—increased student 
                        inquiries by 20% and mentored teams to 2x sales targets. Passionate about building ethically responsible AI 
                        that solves real-world problems.
                    </p>
                ''',
                'order': 1,
            },
            
            # Education
            {
                'category': 'education',
                'title': 'MSc Information Systems',
                'subtitle': 'University College Dublin (UCD)',
                'description': '''
                    <p class="mb-2"><strong>Focus Areas:</strong></p>
                    <ul class="list-disc list-inside space-y-1">
                        <li>AI Ethics</li>
                        <li>Language Models</li>
                        <li>Interactive Dashboards</li>
                        <li>Quantitative Data Analysis</li>
                    </ul>
                ''',
                'date_start': 'Sep 2025',
                'date_end': 'Sep 2026',
                'order': 1,
            },
            {
                'category': 'education',
                'title': 'Bachelor of Computer Applications',
                'subtitle': 'Amity University, Lucknow',
                'description': '''
                    <p class="mb-2"><strong>Focus Areas:</strong></p>
                    <ul class="list-disc list-inside space-y-1">
                        <li>Data Structures</li>
                        <li>Object-Oriented Programming (Java/Python)</li>
                        <li>Software Engineering</li>
                    </ul>
                ''',
                'date_start': 'Sep 2020',
                'date_end': 'Sep 2023',
                'order': 2,
            },
            
            # Experience
            {
                'category': 'experience',
                'title': 'Strategy and Operations Manager',
                'subtitle': 'EduAbroad (Chaos Consulting)',
                'description': '''
                    <p class="mb-3"><strong>Key Achievement:</strong></p>
                    <p>Increased student inquiries by <span class="text-green-400 font-bold">20%</span> and reduced 
                    manual reporting time by <span class="text-green-400 font-bold">30%</span> using automation 
                    tools like Trello and Zoho.</p>
                ''',
                'date_start': 'Nov 2024',
                'date_end': 'Jun 2025',
                'technologies': 'Trello, Zoho, Automation, Strategy',
                'order': 1,
            },
            {
                'category': 'experience',
                'title': 'Associate Team Leader',
                'subtitle': 'EduGorilla Community',
                'description': '''
                    <p class="mb-3"><strong>Key Achievement:</strong></p>
                    <p>Mentored <span class="text-blue-400 font-bold">4 BDAs</span> and achieved 
                    <span class="text-green-400 font-bold">2x team sales targets</span> twice.</p>
                ''',
                'date_start': 'Jun 2024',
                'date_end': 'Oct 2024',
                'technologies': 'Leadership, Sales, Mentoring',
                'order': 2,
            },
            {
                'category': 'experience',
                'title': 'Business Development Associate',
                'subtitle': 'EduGorilla Community',
                'description': '''
                    <p class="mb-3"><strong>Key Achievement:</strong></p>
                    <p>Consistently exceeded sales targets (<span class="text-green-400 font-bold">2x monthly 
                    targets thrice</span>) using CRM pipeline tracking.</p>
                ''',
                'date_start': 'Sep 2023',
                'date_end': 'May 2024',
                'technologies': 'CRM, Sales, Pipeline Management',
                'order': 3,
            },
            
            # Projects
            {
                'category': 'project',
                'title': 'Climate Migration Detection',
                'subtitle': 'Research Project under Prof. Elisa D\'Amico',
                'description': '''
                    <p class="mb-3">Pilot project validating signals of <strong>climate-induced migration</strong> 
                    using geospatial and NLP analysis.</p>
                    <p class="text-gray-400 text-sm">Analyzing Meta/Google Mobility data combined with GDELT/ReliefWeb 
                    news sources to detect climate migration patterns.</p>
                ''',
                'technologies': 'Python, Geospatial Data, NLP, GDELT, ReliefWeb, GeoPandas',
                'order': 1,
            },
            {
                'category': 'project',
                'title': 'Hindi Chatbot with Sentiment Analysis',
                'subtitle': 'NLP Research Project',
                'description': '''
                    <p class="mb-3">Developed a chatbot for <strong>emotion detection in Hindi text</strong> 
                    using RAG architecture and OpenAI API.</p>
                    <p class="text-gray-400 text-sm">Implements Discourse Relations algorithms for improved 
                    contextual understanding.</p>
                ''',
                'technologies': 'Python, Django, RAG, OpenAI API, NLP, Sentiment Analysis',
                'order': 2,
            },
            {
                'category': 'project',
                'title': 'Intelligent Context Compression Engine for LLMs',
                'subtitle': 'Cost Optimization System',
                'description': '''
                    <p class="mb-3">System that reduced LLM API costs by <span class="text-green-400 font-bold">60%</span> 
                    while maintaining <span class="text-blue-400 font-bold">92% answer quality</span>.</p>
                    <p class="text-gray-400 text-sm">Uses Random Forest Classifier with Semantic Compression 
                    techniques.</p>
                ''',
                'technologies': 'Python, Random Forest, Scikit-learn, Semantic Compression, ML',
                'order': 3,
            },
            
            # Publications
            {
                'category': 'publication',
                'title': 'Enhancing Well-Being Through Computational Emotion Analysis in Hindi Language Texts',
                'subtitle': 'Springer Publication',
                'description': '''
                    <p class="mb-3">Published research on computational methods for analyzing emotional content 
                    in Hindi language texts to enhance well-being applications.</p>
                    <p class="text-blue-400">📚 Published in Springer</p>
                ''',
                'technologies': 'NLP, Sentiment Analysis, Hindi, Research',
                'order': 1,
            },
            
            # Skills
            {
                'category': 'skill',
                'title': 'Programming Languages',
                'subtitle': 'Core Technical Skills',
                'description': '''
                    <div class="flex flex-wrap gap-2">
                        <span class="px-3 py-1 bg-blue-600/30 rounded-full text-blue-300">Python</span>
                        <span class="px-3 py-1 bg-yellow-600/30 rounded-full text-yellow-300">SQL</span>
                        <span class="px-3 py-1 bg-orange-600/30 rounded-full text-orange-300">Java</span>
                    </div>
                ''',
                'technologies': 'Python, SQL, Java',
                'order': 1,
            },
            {
                'category': 'skill',
                'title': 'AI & Machine Learning',
                'subtitle': 'Specialization Areas',
                'description': '''
                    <div class="flex flex-wrap gap-2">
                        <span class="px-3 py-1 bg-purple-600/30 rounded-full text-purple-300">NLP</span>
                        <span class="px-3 py-1 bg-purple-600/30 rounded-full text-purple-300">RAG</span>
                        <span class="px-3 py-1 bg-purple-600/30 rounded-full text-purple-300">Scikit-learn</span>
                        <span class="px-3 py-1 bg-purple-600/30 rounded-full text-purple-300">Random Forest</span>
                        <span class="px-3 py-1 bg-purple-600/30 rounded-full text-purple-300">Sentiment Analysis</span>
                    </div>
                ''',
                'technologies': 'NLP, RAG, Scikit-learn, Random Forest, Sentiment Analysis',
                'order': 2,
            },
            {
                'category': 'skill',
                'title': 'Data Science & Visualization',
                'subtitle': 'Analytics Tools',
                'description': '''
                    <div class="flex flex-wrap gap-2">
                        <span class="px-3 py-1 bg-green-600/30 rounded-full text-green-300">Pandas</span>
                        <span class="px-3 py-1 bg-green-600/30 rounded-full text-green-300">GeoPandas</span>
                        <span class="px-3 py-1 bg-green-600/30 rounded-full text-green-300">Matplotlib</span>
                        <span class="px-3 py-1 bg-green-600/30 rounded-full text-green-300">Seaborn</span>
                    </div>
                ''',
                'technologies': 'Pandas, GeoPandas, Matplotlib, Seaborn',
                'order': 3,
            },
            {
                'category': 'skill',
                'title': 'Web Development',
                'subtitle': 'Frameworks & Tools',
                'description': '''
                    <div class="flex flex-wrap gap-2">
                        <span class="px-3 py-1 bg-teal-600/30 rounded-full text-teal-300">Django</span>
                        <span class="px-3 py-1 bg-teal-600/30 rounded-full text-teal-300">REST APIs</span>
                        <span class="px-3 py-1 bg-teal-600/30 rounded-full text-teal-300">Git</span>
                    </div>
                ''',
                'technologies': 'Django, APIs, Git',
                'order': 4,
            },
        ]

        for item_data in items:
            PortfolioItem.objects.create(**item_data)
        
        self.stdout.write(self.style.SUCCESS(f'Successfully seeded {len(items)} portfolio items!'))
